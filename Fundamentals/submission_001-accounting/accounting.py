import sys
import user.authentication
import transactions.journal
import banking

#import banking.reconciliation
#import banking.fvb.reconciliation
#import banking.ubsa.reconciliation
#import banking.online.reconciliation

if __name__ == "__main__":
    #help("modules")
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            print(sys.argv[i])

    user.authentication.authenticate_user()
    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)
    banking.do_reconciliation()

    #banking.reconciliation.do_reconciliation()
    #banking.fvb.reconciliation.do_reconciliation()
    #banking.ubsa.reconciliation.do_reconciliation()
    #banking.online.reconciliation.do_reconciliation()


