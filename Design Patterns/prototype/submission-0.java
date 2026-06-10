interface Shape {
    Shape clone();
}

class Rectangle implements Shape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return this.width;
    }

    public int getHeight() {
        return this.height;
    }

    @Override
    public Shape clone() {
        // Write your code here
        return new Rectangle(this.getWidth(), this.getHeight());
    }
}

class Square implements Shape {
    private int length;

    public Square(int length) {
        this.length = length;
    }

    public int getLength() {
        return this.length;
    }

    @Override
    public Shape clone() {
        // Write your code here
        return new Square(this.getLength());
    }
}

class Test {
    public List<Shape> cloneShapes(List<Shape> shapes) {
        // Write your code here

        List<Shape> cloneShapes = new ArrayList<>();

        for (Shape shape: shapes){
            Shape s = shape.clone();
            cloneShapes.add(s);
        }

        return cloneShapes;
    }
}
