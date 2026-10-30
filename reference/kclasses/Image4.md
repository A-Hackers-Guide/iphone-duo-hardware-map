# `Image4`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.security.Image4`](../kexts/com.apple.security.Image4.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000ba21d10`; metaclass vtable `0xfffffe000848a278`; class vtable `0xfffffe0008489d20`
- Registration (init): `0xfffffe000a8efe20`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Image4` in [`com.apple.security.Image4`](../kexts/com.apple.security.Image4.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `defaults`, `IOMatchCategory` = `Image4`

## Device-tree nodes it binds (1) [DT]

- [`/defaults`](../devicetree/root__defaults.md) on `defaults`

## Strings in its kext that name it (60)

- `Image4: manifest evaluation: unexpected property\n`
- `Image4: payload evaluation: starting trust evaluation\n`
- `Image4:  resetting: %s\n`
- `Image4: manifest evaluation: attempting 'rpnh' policy\n`
- `Image4: manifest evaluation: unable to get domain from manifest: %u\n`
- `\"Image4: unable to allocate memory descriptor for cipher-text: %lu\" @%s:%d`
- `\"Image4: nonce digest too large for PPL: %lu\" @%s:%d`
- `Image4: payload evaluation: '%c%c%c%c' mismtch\n`
- `Image4: payload evaluation: auxiliary evaluation successful\n`
- `Image4: system does not have a supported legacy blob\n`
- `Image4: platform does not support NVRAM\n`
- `static IOReturn Image4UserClient::objectLoad(OSObject *, void *, IOExternalMethodArguments *)`
- `Image4: manifest evaluation: unable to obtain previous stage digest: %u\n`
- `Image4: unable to acquire Diavlo Root CA from expert: %u\n`
- `Image4: unexpected version of legacy digest: %u\n`
- `Image4: unexpected length for legacy digest: %llu\n`
- `Image4: unable to load local policy: %u\n`
- `\"Image4: unable to setup /chosen/manifest-properties node\" @%s:%d`
- `Image4: manifest evaluation: failed: %d, %u\n`
- `Image4: manifest evaluation: failed subsequent stage anti-replay: %u\n`
- `Image4: unable to hash cipher-text: %u\n`
- `Image4: unable to read nonce data from storage: %u\n`
- `Image4: unexpected version for nonce seed blob: V2 | %u\n`
- `Image4: error generating proposal with AppleImage4: %d\n`
- `Image4: manifest evaluation: unable to obtain environment OS version: %u\n`
- `Image4: %s: unable to copyin payload\n`
- `Image4: manifest evaluation: nonce type: %u\n`
- `Image4: unable to parse digest for nonce seed blob: V2 | %u\n`
- `\"Image4: unable to cast service as IODTNVRAM\" @%s:%d`
- `Image4: manifest evaluation: restore-info tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: starting anti-replay evaluation\n`
- `Image4: payload evaluation: property mismatch: %u\n`
- `\"Image4: unable to setup /defaults node in PPL\" @%s:%d`
- `Image4: manifest evaluation: nonce tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: unable to resolve a valid decode implementation\n`
- `Image4: successfully loaded local policy on the system\n`
- `Image4: owning task is not entitled for user-client access\n`
- `\"Image4: attempted to set nonce digest without PPL mutable buffer\" @%s:%d`
- `\"Image4: attempted to get product without PPL context\" @%s:%d`
- `Image4: payload evaluation: starting signature evaluation: %s\n`
- `\"Image4: unable to prepare memory descriptor for plain-text: %d\" @%s:%d`
- `Image4: unable to allocate legacy environment\n`
- `Image4: manifest evaluation: insufficient space for manifest hash\n`
- `\"Image4: unable to allocate memory descriptor for plain-text: %lu\" @%s:%d`
- `Image4: supplementary Root CA already exists: %u\n`
- `\"Image4: unexpected length of PPL mutable buffer: %lu\" @%s:%d`
- `\"Image4: invalid nonce type for setting digest: %u\" @%s:%d`
- `Image4: manifest evaluation: domain tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: manifest tag: '%c%c%c%c'\n`
- `Image4: manifest evaluation: attempting subsequent stage anti-replay policy: %u\n`
- `Image4: unable to parse digest for nonce seed blob: V1 | %u\n`
- `Image4: unable to allocate kernel thread for NVRAM write\n`
- `Image4: manifest evaluation: '%c%c%c%c' mismatch\n`
- `Image4: manifest evaluation: manifest enables mix-and-match\n`
- `Image4: platform booting under NeRD\n`
- `Image4: darwin pseudo-expert: unable to provide UniqueDeviceID [ChipID]\n`
- `Image4: manifest evaluation: enforcing cryptex1 nonce\n`
- `\"Image4: attempted to get defaults without PPL context\" @%s:%d`
- `Image4: manifest evaluation: unable to obtain manifest version: %u\n`
- `Image4: payload evaluation: failed to get payload type: %d\n`
