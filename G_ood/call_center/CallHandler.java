import java.util.ArrayList;

public class CallHandler {

    ArrayList<Manager> managers;
    ArrayList<Director> directors;
    ArrayList<Respondent> respondents;

    ArrayList<ArrayList<? extends Employee>> employeeList;

    ArrayList<Call> callQueue;

    
    private final int HIERARCHY_LEVEL = 3;
    private final int NUM_RESPONDENTS = 10;
    private final int NUM_MANAGERS = 4;
    private final int NUM_DIRECTORS= 2;
    

    public CallHandler() {
        this.callQueue = new ArrayList<Call>();
        this.managers = new ArrayList<Manager>();
        this.directors = new ArrayList<Director>();
        this.respondents = new ArrayList<Respondent>();
        this.employeeList = new ArrayList<ArrayList<? extends Employee>>();

        for (int level = 0; level < this.HIERARCHY_LEVEL; level++) {
            if (level == 0) {
                for (int respondent = 0; respondent < this.NUM_RESPONDENTS; respondent++) {
                    respondents.add(new Respondent("Respondent nr: "+Integer.toString(respondent)));
                }
                this.employeeList.add(respondents);
            }
            if (level == 1) {
                for (int manager = 0; manager < this.NUM_MANAGERS; manager++) {
                    respondents.add(new Respondent("Manager nr: "+Integer.toString(manager)));
                }
                this.employeeList.add(managers);
            }
            if (level == 2) {
                for (int director = 0; director < this.NUM_DIRECTORS; director++) {
                    respondents.add(new Respondent("Director nr: "+Integer.toString(director)));
                }
                this.employeeList.add(directors);
            }
        }
    }

    public Employee insertCall(Call newCall) throws Exception {
        this.callQueue.add(newCall);
        return this.dispatchCall(newCall);
    }


    public Employee dispatchCall(Call call) throws Exception {
        for (int level = 0; level < this.employeeList.size(); level++) {
            for (int respondent = 0; respondent < this.employeeList.get(level).size(); respondent++) {
                Employee empl = this.employeeList.get(level).get(respondent);
                if (empl.isFree() == true) {
                    empl.assignCall(call);
                    return empl;
                }
            }
        }
        throw new Exception();
    }

    // public static void main(final String[] args) {

    //     final CallHandler callHandler = new CallHandler();
    //     for (int i = 0; i < 50; i++) {
    //         Call c = new Call(i);
    //         try {
    //             final Employee resp = callHandler.insertCall(c);
    //             System.out.println(resp.getName());
    //         } catch (Exception e) {
    //             System.out.println("call number "+Integer.toString(i)+" could not have been handeled.");
    //         }
    //     }
    // }
}