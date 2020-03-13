
public abstract class Employee {

    String _name;
    Boolean _free;
    Call _call;

    public Employee(String name) {
        this._name = name;
        this._free = true;
    }

    public void assignCall(Call call) {
        this._call = call;
        this._free = false;
    }


    public Boolean isFree() { return this._free; }
    public String getName() { return this._name; }
}