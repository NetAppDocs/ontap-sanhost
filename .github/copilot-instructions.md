## Copilot instructions for ONTAP SAN Host Utilities documentation

### Repository overview
Product: ONTAP SAN Host Utilities

ONTAP SAN Host Utilities is NetApp software that enables SAN hosts to connect to ONTAP storage systems using the FC and iSCSI protocols. Configure SAN hosts to use SAN Host Utilities to help manage and monitor LUNs and host bus adapters (HBAs). Configure host operating systems to use the NVMe over Fabrics (NVMe-oF) protocol.

### Repository structure

- `_include/hu/` – Reusable AsciiDoc include fragments for Host Utilities content (multipathing, iSCSI, SAN booting, install steps, recommendations)
- `_include/nvme/` – Reusable AsciiDoc include fragments for NVMe-oF content (configure, validate, enable SAN booting, secure in-band auth)
- `_include/windows/` – Reusable AsciiDoc include fragments for Windows Host Utilities install chunks and multipathing
- `media/` – Image assets referenced by documentation pages
- `redirects/` – URL redirect mappings for the published site

### Product-specific context

**Architecture and components:**
- ONTAP is the storage operating system; SAN hosts connect to ONTAP storage using a SAN protocol (FC, FCoE, iSCSI, or NVMe-oF)
- *SAN Host Utilities* are OS-specific software packages (AIX, Linux, Solaris, HP-UX, Windows) that install on the host. AIX, Linux, Solaris, HP-UX provide the `sanlun` CLI toolkit. Windows provides the recommended HBA and registry settings
- *Linux Host Utilities* and *Windows Host Utilities* are the versioned installer packages; Linux Host Utilities installs the `sanlun` utility and sets multipath parameters, Windows Host Utilities sets Windows registry and HBA parameters
- The `sanlun` utility provides CLI commands to list ONTAP LUNs mapped to a host, display multipath information, and retrieve HBA details; it is installed automatically with the Host Utilities package
- *NVMe-oF* configuration is documented separately from FCP/iSCSI and does not use the Host Utilities installer
- On Linux, *dm-multipath* is used for SCSI LUNs (FCP/iSCSI) while native NVMe multipathing is used for NVMe-oF namespaces; both can coexist on the same host
- ONTAP storage can be on-premises or cloud-based (Cloud Volumes ONTAP, Amazon FSx for NetApp ONTAP); in cloud contexts hosts are referred to as *clients*

**Key concepts:**
- *LUN* – Logical unit number; the storage object presented to a SAN host over FC or iSCSI
- *Namespace* – The NVMe-oF equivalent of a LUN, presented over NVMe/FC or NVMe/TCP
- *HBA (Host Bus Adapter)* – The host-side FC adapter; supported vendors include Broadcom/Emulex and Marvell/QLogic
- *Multipathing* – Redundant path configuration to storage; on Linux this is managed by `/etc/multipath.conf` for FCP and SCSI and ANA for NVME-oF; on AIX, HP-UX, Solaris, and Windows by MPIO
- *SAN booting* – Booting the host OS from a LUN or namespace on ONTAP storage over the SAN fabric
- *igroup (initiator group)* – An ONTAP object that maps LUNs to specific host initiators
- *NVMe subsystem* – The ONTAP-side object that maps NVMe namespaces to host NQNs
- *hostnqn* – The NVMe Qualified Name identifying the host; stored in `/etc/nvme/hostnqn` on Linux
- *ASA (All SAN Array)* – A NetApp storage architecture where all paths are active-active; configuration details for ASA differ from AFF/FAS in multipath settings

**Naming conventions and terminology:**

- NVMe transport variants: *NVMe/FC* (NVMe over Fibre Channel) and *NVMe/TCP* (NVMe over TCP); collectively referred to as *NVMe-oF* (NVMe over Fabrics)
- FC protocol is also referred to as *FCP* (Fibre Channel Protocol) in sidebar and keywords
- Broadcom/Emulex driver is *lpfc*; Marvell/QLogic driver is *qla2xxx*

### Typical user workflows

**Install SAN Host Utilities and configure FCP/iSCSI (Linux):** Verify IMT-supported configuration → Install Linux Host Utilities package → Configure dm-multipath for ONTAP LUNs → Configure iSCSI (if applicable) → Optionally exclude devices from multipathing → Customize multipath parameters

**Install Windows Host Utilities:** Verify supported configuration in IMT → Install required Windows hotfixes → Add iSCSI or FCP license on ONTAP → Install WUHU package (sets registry and HBA parameters) → Verify host connectivity

**Configure NVMe-oF on Linux:** Optionally enable SAN booting → Install OS and verify `nvme-cli` package → Configure NVMe/FC or NVMe/TCP → Validate NVMe-oF namespaces and multipath → Optionally configure secure in-band authentication (NVMe/TCP)

**Configure NVMe-oF on Windows:** Enable MPIO for NVMe → Configure NVMe/FC or NVMe/TCP initiator → Validate NVMe-oF namespaces and connectivity
