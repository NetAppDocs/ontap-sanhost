## Copilot instructions for ONTAP SAN Host Utilities documentation

### Repository overview
Product: ONTAP SAN Host Utilities

ONTAP SAN Host Utilities is NetApp software that enables SAN hosts to connect to ONTAP storage systems using the FC and iSCSI protocols. Configure SAN hosts to use SAN Host Utilities to help manage and monitor LUNs and host bus adapters (HBAs). Configure host operating systems to use the NVMe over Fabrics (NVMe-oF) protocol.

### Repository structure
- `hu-aix-*.adoc` – AIX Host Utilities installation and configuration pages (SAN booting, multipathing)
- `hu-centos-*.adoc` – CentOS FCP and iSCSI host configuration pages
- `hu-hpux-*.adoc` / `hu_hpux_*.adoc` – HP-UX Host Utilities installation and command reference pages
- `hu-luhu-*.adoc` / `hu_luhu_*.adoc` – Linux Host Utilities installation, `sanlun` utility, and command reference pages
- `hu-ol-*.adoc` – Oracle Linux FCP and iSCSI host configuration pages
- `hu-proxmox-*.adoc` – Proxmox VE FCP and iSCSI host configuration pages
- `hu-rhel-*.adoc` – RHEL FCP and iSCSI host configuration pages
- `hu-rockylinux-*.adoc` – Rocky Linux FCP and iSCSI host configuration pages
- `hu-sles-*.adoc` – SUSE Linux Enterprise Server FCP and iSCSI host configuration pages
- `hu-solaris-*.adoc` / `hu_solaris_*.adoc` – Solaris Host Utilities installation and command reference pages
- `hu-veritas-*.adoc` / `hu_veritas_*.adoc` – Veritas Infoscale and Storage Foundation configuration pages
- `hu-windows-*.adoc` / `hu_windows_*.adoc` – Windows FCP and iSCSI host configuration pages
- `hu-wuhu-*.adoc` / `hu_wuhu_*.adoc` – Windows Host Utilities (WUHU) installation, upgrade, repair/remove, troubleshoot, and configuration pages
- `hu_citrix_*.adoc` – Citrix XenServer/Hypervisor FCP and iSCSI host configuration pages
- `hu_vsphere_*.adoc` – VMware vSphere (ESXi) FCP and iSCSI host configuration pages
- `hu_ubuntu_*.adoc` – Ubuntu FCP and iSCSI host configuration pages
- `nvme-*.adoc` – NVMe-oF host configuration pages (NVMe/FC and NVMe/TCP) for Linux, ESXi, AIX, and Windows hosts
- `nvme-*-supported-features.adoc` – Per-OS pages listing ONTAP support and feature availability for NVMe-oF
- `_include/hu/` – Reusable AsciiDoc include fragments for Host Utilities content (multipathing, iSCSI, SAN booting, install steps, recommendations)
- `_include/nvme/` – Reusable AsciiDoc include fragments for NVMe-oF content (configure, validate, enable SAN booting, secure in-band auth)
- `_include/windows/` – Reusable AsciiDoc include fragments for Windows Host Utilities install chunks and multipathing
- `media/` – Image assets referenced by documentation pages
- `redirects/` – URL redirect mappings for the published site
- `overview.adoc` – Top-level introduction to SAN host configurations
- `hu_sanhost_index.adoc` – Index page for SAN Host Utilities software
- `hu_fcp_scsi_index.adoc` – Index page for FCP and iSCSI host configuration
- `hu-nvme-index.adoc` – Index page for NVMe-oF host configuration
- `troubleshoot.adoc` – NVMe-oF troubleshooting for Linux hosts
- `project.yml` – Site settings and sidebar navigation structure
- `_index.yml` – Landing page configuration

### Product-specific context

**Architecture and components:**
- ONTAP is the storage operating system; SAN hosts connect to ONTAP storage using a SAN protocol (FC, FCoE, iSCSI, or NVMe-oF)
- *SAN Host Utilities* are OS-specific software packages (AIX, Linux, Solaris, HP-UX, Windows) that install on the host. AIX, Linux, Solaris, HP-UX provide the `sanlun` CLI toolkit. Windows provides the recommended HBA and registry settings
- *Linux Host Utilities* (LUHU) and *Windows Host Utilities* (WUHU) are the versioned installer packages; LUHU installs the `sanlun` utility and sets multipath parameters, WUHU sets Windows registry and HBA parameters
- The `sanlun` utility provides CLI commands to list ONTAP LUNs mapped to a host, display multipath information, and retrieve HBA details; it is installed automatically with the Host Utilities package
- *NVMe-oF* configuration is documented separately from FCP/iSCSI and does not use the Host Utilities installer; it relies on the native `nvme-cli` package on Linux hosts
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
- Linux Host Utilities package name: `netapp_linux_unified_host_utilities`
- Windows Host Utilities is abbreviated *WUHU*; file pages use the `hu-wuhu-` or `hu_wuhu_` prefix
- Linux Host Utilities is abbreviated *LUHU*; file pages use the `hu-luhu-` or `hu_luhu_` prefix
- NVMe-oF page filenames use the `nvme-` prefix followed by the OS name (e.g., `nvme-rhel-9x.adoc`, `nvme-ol-10x.adoc`)
- FCP/iSCSI host configuration pages use the `hu-` prefix followed by OS abbreviation and major version pattern (e.g., `hu-rhel-9x.adoc`, `hu-ol-10x.adoc`)
- Older pages in the repository use underscores in filenames (`hu_rhel_`, `hu_windows_`); newer pages use hyphens (`hu-rhel-`, `hu-windows-`)
- NVMe transport variants: *NVMe/FC* (NVMe over Fibre Channel) and *NVMe/TCP* (NVMe over TCP); collectively referred to as *NVMe-oF* (NVMe over Fabrics)
- FC protocol is also referred to as *FCP* (Fibre Channel Protocol) in sidebar and keywords
- *sanlun* commands follow the pattern: `sanlun lun show`, `sanlun fcp show adapter`
- Broadcom/Emulex driver is *lpfc*; Marvell/QLogic driver is *qla2xxx*

### Typical user workflows

**Install SAN Host Utilities and configure FCP/iSCSI (Linux):** Verify IMT-supported configuration → Install Linux Host Utilities package → Configure dm-multipath for ONTAP LUNs → Configure iSCSI (if applicable) → Optionally exclude devices from multipathing → Customize multipath parameters

**Install Windows Host Utilities:** Verify supported configuration in IMT → Install required Windows hotfixes → Add iSCSI or FCP license on ONTAP → Install WUHU package (sets registry and HBA parameters) → Verify host connectivity

**Configure NVMe-oF on Linux:** Optionally enable SAN booting → Install OS and verify `nvme-cli` package → Configure NVMe/FC or NVMe/TCP → Validate NVMe-oF namespaces and multipath → Optionally configure secure in-band authentication (NVMe/TCP)

**Configure NVMe-oF on Windows:** Enable MPIO for NVMe → Configure NVMe/FC or NVMe/TCP initiator → Validate NVMe-oF namespaces and connectivity
