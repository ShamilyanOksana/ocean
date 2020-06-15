pragma solidity >0.5.0;

contract Ocean{

    address public admin = msg.sender;

    struct Home {
        uint ID_home;
        address owner;
        string info;
        uint square;
        uint period;
        uint in_sale;
    }

    struct Sale {
        uint ID_sale;
        uint ID_home;
        address payable seller;
        address payable buyer;
        uint price;
        uint status;        // 0 - stoped, 1 - active, 2 - finished
    }

    Home[] public homes;
    Sale[] public sales;

    modifier Admin {
        require(msg.sender == admin, "Not admin");
        _;
    }

    function reg_home(address owner, string memory info, uint square, uint period) public Admin {
        uint ID_home = homes.length;
        homes.push(Home(ID_home, owner, info, square, period, 0));
    }


    function create_sale(uint ID_home, uint price) public {
        uint in_sale = homes[ID_home].in_sale;
        require(in_sale == 0, 'Уже продается');
        address owner = homes[ID_home].owner;
        require(msg.sender == owner);
        uint ID_sale = sales.length;
        address payable seller = msg.sender;
        address payable buyer = 0x0000000000000000000000000000000000000000;
        uint status = 1;
        sales.push(Sale(ID_sale, ID_home, seller, buyer, price, status));
        homes[ID_home].in_sale = 1;
    }

    function stop_sale(uint ID_sale) public {
        uint status = sales[ID_sale].status;
        require(status == 1);
        address payable seller = sales[ID_sale].seller;
        require(msg.sender == seller);
        sales[ID_sale].status = 0;
        uint ID_home = sales[ID_sale].ID_home;
        homes[ID_home].in_sale = 0;

    }

    function buy(uint ID_sale) public payable {
        uint price = sales[ID_sale].price;
        require(msg.value == price, "Wrong money");
        uint status = sales[ID_sale].status;
        require(status == 1);
        address payable seller = sales[ID_sale].seller;
        require(msg.sender != seller);
        sales[ID_sale].buyer = msg.sender;
        sales[ID_sale].status = 2;
    }

    function get_sale(uint ID_sale) public view returns(uint, address payable, address payable, uint, uint) {
        return(sales[ID_sale].ID_home, sales[ID_sale].seller, sales[ID_sale].buyer, sales[ID_sale].price, sales[ID_sale].status);
    }

    function get_home(uint ID_home) public view returns(address, string memory, uint, uint, uint) {
        return(homes[ID_home].owner, homes[ID_home].info, homes[ID_home].square, homes[ID_home].period, homes[ID_home].in_sale);
    }

    function get_homes_amount() public view returns(uint) {
        return(homes.length);
    }

    function get_sales_amount() public view returns(uint) {
        return(sales.length);
    }

}