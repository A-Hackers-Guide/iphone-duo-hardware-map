# `/filesystems/fstab-ephemeral-devrecov-data/preboot-vol`

- Name: `preboot-vol`
- Parent: [`/filesystems/fstab-ephemeral-devrecov-data`](root__filesystems__fstab-ephemeral-devrecov-data.md)
- phandle: `500`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (9) [DT]

- **`AAPL,phandle`**: `500` (`0x1f4`) → phandle of [`/filesystems/fstab-ephemeral-devrecov-data/preboot-vol`](root__filesystems__fstab-ephemeral-devrecov-data__preboot-vol.md)
- **`name`**: `preboot-vol`
- **`vol.fs_file`**: `/private/preboot`
- **`vol.fs_mntopts`**: `nosuid,nodev,nobrowse`
- **`vol.fs_mntorder`**: `1` (`0x1`)
- **`vol.fs_name`**: `Preboot`
- **`vol.fs_passno`**: `1` (`0x1`)
- **`vol.fs_role`**: `16` (`0x10`)
- **`vol.fs_type`**: `ro`
