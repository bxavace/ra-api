"""Seeder for risk response options and guidance statements."""
from app.models import db, RiskResponse

def seed_risks():
    """Populate risk response options and guidance statements."""
    if RiskResponse.query.first() is not None:
        print("Risk responses already seeded. Skipping...")
        return
    responses = [
        {
            "name": "Accept",
            "guidance": "If the level of risk meets the risk acceptance criteria, there is no need for implementing additional controls and the risk can be retained.",
        },
        {
            "name": "Avoid",
            "guidance": "When the identified risks are considered too high, or the costs of implementing other risk treatment options exceed the benefits, a decision may be made to avoid the risk completely, by withdrawing from a planned or existing activity or set of activities, or changing the conditions under which the activity is operated. For example, for risks caused by nature it may be most cost effective alternative to physically move the information processing facilities to a place where the risk does not exist or is under control.",
        },
        {
            "name": "Close",
            "guidance": "In order to choose this response, either the Total Probability or the Impact must be completely eliminated through change(s) to the process, solutions, etc.",
        },
        {
            "name": "Mitigate",
            "guidance": "Mitigation plans should take the following considerations into account:\n\nCost\n* During control selection it is important to weigh the cost of acquisition, implementation, administration, operation, monitoring, and maintenance of the controls against the value of the assets being protected\n* The return on investment in terms of risk reduction and potential to exploit new business opportunities afforded by certain controls should be considered.\n* Consideration should be given to specialized skills that may be needed to define and implement new controls or modify existing ones.\n\nTechnical\n* Technical constraints such as performance requirements, manageability (operational support requirements) and compatibility issues may hamper the use of certain controls or could induce human error either nullifying the control, giving a false sense of security or even increasing the risk beyond not having the control (e.g. requiring complex passwords without proper training, leading to users writing passwords down)\n\nType of Protection\n* Correction, elimination, prevention, impact minimization, deterrence, detection, recovery, monitoring and awareness.\n\nConstraints\n* Time, Financial, Technical, Operational, Cultural, Ethical, Environmental, Legal, Ease of use, Personnel, Constraints for integrating new and existing controls",
        },
        {
            "name": "Transfer",
            "guidance": "Risk transfer involves a decision to share certain risks with external parties. Risk transfer can create new risks or modify Transfer can be done by insurance that will support the consequences, or by sub-contracting a partner whose role will be to monitor the information system and take immediate actions to stop an attack before it makes a defined level of damage.\nIt should be noted that it may be possible to transfer the responsibility to manage risk but it is not normally possible to transfer the liability of an impact. Customers will usually attribute an adverse impact as being the fault of the organization.",
        },
    ]
    for resp in responses:
        db.session.add(RiskResponse(**resp))
    db.session.commit()
    print("✓ Risk responses seeded.")
