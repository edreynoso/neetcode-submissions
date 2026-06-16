class Solution {

    public record Tuple(int position, double hours){}

    public int carFleet(int target, int[] position, int[] speed) {

        Tuple[] cars = new Tuple[position.length];
        
        for (int i = 0; i < position.length; i++){
            double hour = (double) (target - position[i]) / speed[i];

            Tuple tup = new Tuple(position[i], hour);

            cars[i] = tup;

        }

        Deque<Tuple> stack = new ArrayDeque();

        Arrays.sort(cars, Comparator.comparingInt(Tuple::position));

        stack.push(cars[cars.length-1]);

        for (int i = cars.length -1; i >= 0; i--){

            if (cars[i].hours > stack.peek().hours){
                stack.push(cars[i]);
            }
        }

        return stack.size();

    }
}
