class Wall{

    //벽의 중심점은 top left
    x;
    y;
    size = 12; //벽의 크기
    fillColor = "pink";
    borderColor = "black";

    constructor(x , y){
        this.x = x;
        this.y = y;
    }

    getX() {
        return this.x;
    }
    
    setX(x) {
        this.x = x;
    }

    getY() {
        return this.y;
    }
    
    setY(y) {
        this.y = y;
    }

    getSize(){
        return this.size;
    }

    setSize(size){
        this.size = size;
    }


    getLeft() {
        return this.x;
    }

    getRight() {
        return this.x + this.size;
    }

    getTop() {
        return this.y;
    }

    getBottom() {
        return this.y + this.size;
    }
    
}