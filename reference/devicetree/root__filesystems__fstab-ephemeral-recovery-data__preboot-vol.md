# `/filesystems/fstab-ephemeral-recovery-data/preboot-vol`

- Name: `preboot-vol`
- Parent: [`/filesystems/fstab-ephemeral-recovery-data`](root__filesystems__fstab-ephemeral-recovery-data.md)
- phandle: `489`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (9) [DT]

- **`AAPL,phandle`**: `489` (`0x1e9`) → phandle of [`/filesystems/fstab-ephemeral-recovery-data/preboot-vol`](root__filesystems__fstab-ephemeral-recovery-data__preboot-vol.md)
- **`name`**: `preboot-vol`
- **`vol.fs_file`**: `/private/preboot`
- **`vol.fs_mntopts`**: `nosuid,nodev,nobrowse`
- **`vol.fs_mntorder`**: `1` (`0x1`)
- **`vol.fs_name`**: `Preboot`
- **`vol.fs_passno`**: `1` (`0x1`)
- **`vol.fs_role`**: `16` (`0x10`)
- **`vol.fs_type`**: `ro`
