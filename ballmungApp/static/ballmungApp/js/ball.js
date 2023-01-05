class Ball{

    //실제 공의 중심점은 정가운데임

    x; //x좌표
    y; //y좌표
    size = 4; //반지름
    speed = 0.85; //좌우 이동속도
    xyDir = 1; //공의 좌우 방향 1:오른쪽 -1:왼쪽
    jump = 3; //점프력
    dy = this.jump; //위아래로 이동시키는 값(?)
    gravity = 0.15; //중력값
    isGoal = false; //골인 지역에 도착했는지 여부

    //게임 끝난후 공이 위치할 좌표
    gx = 0;
    gy = 0;

    alpha = 1.0;
    color = "#000000";//색상 기본값은 검정
    rgba = "rgba(0,0,0,1)";
    

    constructor(x, y, speed, jump, gravity, xyDir, color, rgba){
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.jump = jump;
        this.gravity = gravity;
        this.color = color;
        this.rgba = rgba;

        if(xyDir == 0){
            this.xyDir = 1;
        }else{
            this.xyDir = -1;
        }
        
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

    getGX() {
        return this.gx;
    }
    
    setGX(gx) {
        this.gx = gx;
    }

    getGY() {
        return this.gy;
    }
    
    setGY(gy) {
        this.gy = gy;
    }

    getSize(){
        return this.size;
    }

    setSize(size){
        this.size = size;
    }

    getSpeed(){
        return this.speed;
    }

    setSpeed(speed){
        this.speed = speed;
    }
    getXyDir(){
        return this.xyDir;
    }
    setXyDir(xyDir){
        this.xyDir = xyDir;
    }

    getJump(){
        return this.jump;
    }
    setJump(jump){
        this.jump = jump;
    }

    getGravity(){
        return this.gravity;
    }
    setGravity(gravity){
        this.gravity = gravity;
    }

    getDy(){
        return this.dy;
    }
    setDy(dy){
        this.dy = dy;
    }

    getColor(){
        return this.color;
    }
    setColor(color){
        this.color = color;
    }
    
    getRight(){
        return this.x+this.size;
    }
    getLeft(){
        return this.x-this.size;
    }
    getTop(){
        return this.y-this.size;
    }
    getBottom(){
        return this.y+this.size;
    }

    getRightPoint(){
        return {x:this.x+this.size, y:this.y};
    }
    getLeftPoint(){
        return {x:this.x-this.size, y:this.y};
    }
    getTopPoint(){
        return {x:this.x, y:this.y-this.size};
    }
    getBottomPoint(){
        return {x:this.x, y:this.y+this.size};
    }

    getAlpha(){
        return this.alpha
    }
    setAlpha(alpha){
        this.alpha = alpha;
    }

    getRgba(){
        return this.rgba;
    }

    changeColor(){
        const r = parseInt(((this.color).substring(1,3)), 16);
        const g = parseInt(((this.color).substring(3,5)), 16);
        const b = parseInt(((this.color).substring(5,7)), 16);
        this.rgba = `rgba(${r},${g},${b},${this.alpha})`;
    }
}