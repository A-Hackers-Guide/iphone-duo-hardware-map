# `ApplePTDCommon`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePTD`](../kexts/com.apple.driver.ApplePTD.md)
- Object size: `0x40` (64 bytes)
- Metaclass: `0xfffffe000b9883b0`; metaclass vtable `0xfffffe000819d030`; class vtable `0xfffffe000819cfa0`
- Registration (init): `0xfffffe0009378f20`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (15)

- `bool ApplePTDCommon::start(IOService *, IOService *)`
- `IOReturn ApplePTDCommon::_ptdLookupMultiple(ptd_data_entry_t *, uint32_t)`
- `IOReturn ApplePTDCommon::ptdDoCmdOp(ptd_cmd_t, uintptr_t, const ApplePTDAccessor &)`
- `ApplePTDCommon.cpp`
- `IOReturn ApplePTDCommon::_ptdInsertEntry(ptd_data_entry_t *)`
- `bool ApplePTDCommon::init(const char *)`
- `ApplePTDCommon`
- `site.ApplePTDCommon`
- `static SInt32 ApplePTDCommon::_ptdSortFunction(const OSMetaClassBase *, const OSMetaClassBase *, void *)`
- `IOReturn ApplePTDCommon::ptdEntryStruct(OSDictionary *, ptd_data_entry_t *)`
- `IOReturn ApplePTDCommon::_ptdLookupLength(uint32_t, uint32_t *)`
- `IOReturn ApplePTDCommon::_ptdFindAndCheckEntry(ptd_data_entry_t *, ptd_function_args_t *)`
- `IOReturn ApplePTDCommon::_ptdReadMultiple(ptd_function_args_t *, uint32_t, bool, const ApplePTDAccessor &)`
- `IOReturn ApplePTDCommon::appleARMFunctionNew(void *, void *)`
- `IOReturn ApplePTDCommon::ptdDoMultiCmdOp(ptd_cmd_t, uintptr_t, uint64_t, const ApplePTDAccessor &)`
