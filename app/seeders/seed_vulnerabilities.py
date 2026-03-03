"""Seeder for potential vulnerabilities per global process."""
from app.models import db, Vulnerability, GlobalProcess

GP_VULNERABILITIES = {
    "Backup and Restore": """
    Is there a risk of loss of IBM assets and/or disruption to services due to inadequate backup or recovery process caused by:
    * Lack of current backup and recovery plans/procedures
    * Lack of involvement by owner management
    * Lack of media containing recent backup data
    * Lack of tested backup process and media
    """,
    "Configuration Item Build and Decommission": """
    Is there a risk that newly activated systems are not securely configured/hardened due to:
    * Lack of process and/or procedures for ensuring new systems are securely configured to meet all requirements prior to activation
    * Newly activated systems with unresolved security deficiencies
    * Lack of auditable documentation following specified retention requirements
    """,
    "Configuration Management and Security Inventory Management": """
    Is there a risk that security requirements will not be properly implemented on all systems due to a lack of complete and accurate inventory caused by:
    * Missing inventory record
    * Incorrect classification or system configuration information
    """,
    "Disaster Recovery Management": """
    Is there a risk of not being able to recover vital business processes in the event of a physical site incident, natural or man-made disaster, pandemic, or human based incident caused by:
    * Lack of DR plan
    * Lack of Categorization of the Business Criticality Value
    * Lack of criteria for the declaration of disaster, and the procedures to declare a disaster or emergency.
    * Lack of defined roles and responsibilities between the service provider and customer.
    * Lack of results of previous DR test as part of DRP addendum along with customer or reviewer signature and necessary follow-up or update within 6-months.
    * Full  execution DR test  not performed minimum once every 24 months for IBM internal; or as required per customer contractual requirements.
    * Lack of auditable documentation following specified retention requirements
    """,
    "Identity and Access Management": """
    Is there a risk of unauthorized userids or excessive privileges due to:
    * Lack of management authorization for all userids and privileges prior to provisioning
    * Lack of provisioning of unique and complex passwords
    * Lack of prompt removal of user access when no longer required due to employee separations or changes in work assignments
    * Lack of individual accountability for shared userids
    * Lack of periodic employee verification for userid owners
    * Lack of auditable documentation following specified retention requirements
    """,
    "Integrated Service Management": """
    Is there a risk of system hardware, software, and network changes being made without following a complete change management process due to:
    * Lack of a complete plan for implementing a change, including approval, test, install, migration, and backout procedures
    * Lack of review and approval of all submitted changes
    * Lack of change status communication to customer and IBM personnel
    * Lack of adherence to or existence of emergency change management procedure
    * Lack of auditable documentation following specified retention requirements
    """,
    "IT Risk Management": """
    Is there a chance that risks in the environment are not effectively identified and managed caused by:
    * Lack of procedure to assess risk, define secondary controls, and determine when risk should be formalized
    * Lack of risk approval by manager owning process
    * Lack of clear assignment of risk mitigation activities to customer or IBM
    * Lack of an action plan with a reasonable time frame to address specific risks
    * Lack of annual review for risks extending beyond 12 months
    * Lack of auditable documentation following specified retention requirements
    """,
    "None - End of Life / End of Service": """
    Is there a risk in the form of one or more of the following:
    * Security vulnerabilities - The vendor will not provide maintenance, development or security support for the hardware or software.
    * Software incompatibility - Data migrations and or recovery from legacy to latest version would be a challenge.
    * Compliance issues - Not meeting regulatory requirements could result in significant fines or other consequences.
    * Operating challenges -  Challenges to meet contractual service levels, e.g. availability; restoration of service may not be possible or could be delayed.
    """,
    "None - Nonstandard Liability Engagement": """
    Is there a risk of liability due to the proposed nonstandard liability terms and/or the design of the proposed solution:
    * Trigger(s) that causes the clause to be enacted, e.g. thresholds or limits
    * Regulated data, e.g. SPI, PHI, IRS, or CJIS
    * Timing, encryption status, retention, monitoring and/or access of data in IBM custody
    * Scope, labor model, and security responsibilities of service
    * Controls or lack thereof provided by IBM, client, and/or third party services or solutions
    """,
    "None - Offering / Solution": """
    Is there a risk of an insecure offering or solution due to:
    * Environmental issues, e.g. out-of-date operating system, middleware, and/or application software versions and/or patches
    * Existence of world readable files or folders
    * Lack of coding best practices, e.g. missing HTTP security headers and/or cookies not marked ""HttpOnly""
    * Lack of encryption, including passage and/or storage of clear text credentials
    * Use of weak algorithms and/or ciphers
    * Use of weak password policies, lockout mechanisms, and /or related authentication measures"
    """,
    "Other": "Specific vulnerability guidance is not available for the 'Other' Global Process selection.",
    "Patch Management": """
    Is there a risk of system software containing vulnerabilities caused by security advisory patches not being installed within the required time frame due to:
        * Inaccurate system inventory including operating systems, middleware, network devices and devices with firmware or microcode
        * Incorrect determination of advisory applicability
        * Failure to follow change management process when installing advisories
        * Failure to install advisories based on the timetable stated in applicable standards
        * End of life software which is no longer supported
        * Lack of auditable documentation following specified retention requirements
    """,
    "Physical Security": """
    Is there a risk of service interruption, loss, theft, or misuse of assets caused by unauthorized physical access to systems, data, and networks due to:
    * Physical Access without current business need authorization (regular employees, cleaners, visitors, contractors, etc.)
    * Malfunctioning emergency exits and associated alarms
    * Unmanaged key based access
    * Unsecured loading dock areas
    * Unsecured confidential material
    * Lack of auditable documentation following specified retention requirements
    """,
    "Portable Storage Media Ops": """
    Is there a risk of unauthorized copying, damage, loss, destruction or theft of data assets caused by poor management of PSM due to:
    * Lack of accurate inventory via baseline and periodic reconciliation
    * Inventory exceptions not resolved
    * Inventory performed without proper SoD
    * Disposal of media without adequate data destruction
    * Media containing confidential data not labeled as such
    * Physical access to PSM without business need
    * Lack of auditable documentation following specified retention requirements
    etc.
    """,
    "Security Management": """
    Is there a risk of insecure systems and/or software due to incorrect security settings and options caused by:
    * Lack of technical specifications detailing security related settings for all platforms software
    * OSRs that are writable by general users
    * Programs executed with privileged authority that can be updated by general users
    * Failure to execute health check process based on the timetable stated in applicable standards
    * Health check process which does not incorporate all requirements in corporate policies, standards, and guidelines
    * Lack of detailed audit logs which can support incident response and forensics
    * Lack of auditable documentation following specified retention requirements
    """
}

def seed_vulnerabilities():
    """Populate vulnerabilities table with placeholder data."""
    if Vulnerability.query.first() is not None:
        print("Vulnerabilities already seeded. Skipping...")
        return
    # Iterate over the GP_VULNERABILITIES dictionary and create Vulnerability entries
    for gp_name, description in GP_VULNERABILITIES.items():
        global_process = GlobalProcess.query.filter_by(name=gp_name).first()
        if global_process:
            vulnerability = Vulnerability(
                global_process_id=global_process.id,
                description=description,
                is_potential=True
            )
            db.session.add(vulnerability)
        else:
            print(f"Warning: Global Process '{gp_name}' not found. Skipping vulnerability seeding for this process.")
    db.session.commit()
    print("✓ Vulnerabilities seeded.")
