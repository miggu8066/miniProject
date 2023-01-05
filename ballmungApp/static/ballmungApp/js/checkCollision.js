function checkCollision(ball, wall) {

    //공의 아래쪽 좌표와 충돌한 경우
    if (ball.getBottomPoint().x >= wall.getLeft() && ball.getBottomPoint().x <= wall.getRight() && ball.getBottomPoint().y >= wall.getTop() && ball.getBottomPoint().y <= wall.getBottom()) {
        ball.setDy(ball.getJump()); //
        ball.setY(wall.getTop() - ball.getSize());
        //console.log("충돌됨");
    }

    //공의 왼쪽 좌표와 충돌한 경우
    if (ball.getLeftPoint().x >= wall.getLeft() && ball.getLeftPoint().x <= wall.getRight() && ball.getLeftPoint().y >= wall.getTop() && ball.getLeftPoint().y <= wall.getBottom()) {
        ball.setXyDir(ball.getXyDir() * (-1)); //공의 좌우진행방향 바꾸기
        ball.setX(wall.getRight() + ball.getSize()); //공의 위치 조정
        //console.log("충돌됨");
    }

    //공의 오른쪽 좌표와 충돌한 경우
    if (ball.getRightPoint().x >= wall.getLeft() && ball.getRightPoint().x <= wall.getRight() && ball.getRightPoint().y >= wall.getTop() && ball.getRightPoint().y <= wall.getBottom()) {
        ball.setXyDir(ball.getXyDir() * (-1));
        ball.setX(wall.getLeft() - ball.getSize());
        //console.log("충돌됨");
    }

    //공의 위쪽 좌표와 충돌한 경우
    if (ball.getTopPoint().x >= wall.getLeft() && ball.getTopPoint().x <= wall.getRight() && ball.getTopPoint().y >= wall.getTop() && ball.getTopPoint().y <= wall.getBottom()) {
        ball.setDy(-(ball.getDy() * 2 / 3)); //
        ball.setY(wall.getBottom() + ball.getSize());
        //console.log("충돌됨");
    }

    
}