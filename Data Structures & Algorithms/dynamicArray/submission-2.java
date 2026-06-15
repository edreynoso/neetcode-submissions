class DynamicArray {

    private int[] arr;
    private int capacity;
    private int count = 0;

    public DynamicArray (int capacity) {
        this.capacity = capacity;
        this.arr = new int[capacity];
    }

    public int get(int i) {

        return this.arr[i];    

    }

    public void set(int i, int n) {

        if (this.arr[i] == 0){
            count++;
        }

        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (count >= this.capacity){
            resize();
        }

        this.arr[count] = n;
        count++;
    }

    public int popback() {
        int val = this.arr[count-1];
        count--;
        return val;
    }

    private void resize() {

        this.capacity *= 2;

        this.arr = Arrays.copyOf(this.arr, this.capacity);

    }

    public int getSize() {
        return count;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
