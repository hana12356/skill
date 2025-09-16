public class Box {
    public static void main(String[] args){
        Box1<Integer> box=new Box1<>();
        box.setItem(1245);
        System.out.println(box.getItem());
    }
}
class Box1<T>{
    T item;
    public void setItem(T item){
        this.item=item;
    }
    public int getItem(){
        return (int) item;
    }
}
