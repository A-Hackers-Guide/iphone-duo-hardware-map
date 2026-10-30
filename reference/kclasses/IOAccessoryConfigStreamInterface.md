# `IOAccessoryConfigStreamInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0x540` (1,344 bytes)
- Metaclass: `0xfffffe000b9f1150`; metaclass vtable `0xfffffe0008323868`; class vtable `0xfffffe0008323308`
- Registration (init): `0xfffffe0009f82e54`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleC26ConfigStream`](AppleC26ConfigStream.md) — `com.apple.driver.AppleC26Charger`

## Strings in its kext that name it (58)

- `%s:IOAccessoryConfigStreamInterface::%s commandID:%x payloadLength:%02llX sizeof(cmdID)=%lu \n`
- `%s:IOAccessoryConfigStreamInterface::%s _initialRetrievalFinished %d, _numCategories %d, categoryID/Index %x/%d, propertyID/Index %x/%d, infoDataLen %llu, ret %x \n`
- `%s:IOAccessoryConfigStreamInterface::%s %llu bytes, isInactive %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s RetPropertyData: categoryID %x, propertyID %x, _sentPropertyDataRequestWithSleep %d, _initialRetrievalFinished %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s RetDevInfo: ver %u, reserved %x, numOfCategories %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s commandID %x, data(%llu bytes):%s \n`
- `%s:IOAccessoryConfigStreamInterface::%s RetCategoryInfo: index %d, categoryID %x, numProperties %llu, requested index %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s commandID %x, %llu bytes, isInactive %d, status %x \n`
- `%s:IOAccessoryConfigStreamInterface::%s wait for auth! (%d / %d / %d)\n`
- `%s:IOAccessoryConfigStreamInterface::%s auth passed %d, failed %d\n`
- `%s:IOAccessoryConfigStreamInterface::%s Not enabled! (%d / %d / %d) \n`
- `%s:IOAccessoryConfigStreamInterface::%s _numCategories %d, numProperties %d, No properties found for categoryID 0x%04x ! \n`
- `%s:IOAccessoryConfigStreamInterface::%s END \n`
- `%s:IOAccessoryConfigStreamInterface::%s _initialRetrievalFinished %d, _numCategories %d, categoryID/Index %x/%d, propertyID/Index %x/%d, ret %x \n`
- `%s:IOAccessoryConfigStreamInterface::%s _numCategories %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s RetPropertyData: catIndex %d / %d, propIndex %d, categoryID %x, propertyID %x, dataLen %llu, requested ID %x-%x \n`
- `IOAccessoryConfigStreamInterface`
- `%s:IOAccessoryConfigStreamInterface::%s send initial!  (%d / %d / %d)\n`
- `%s:IOAccessoryConfigStreamInterface::%s END success=%d \n`
- `site.IOAccessoryConfigStreamInterface`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID %x, propertyID %x, in commandGate, retrieve propertyData \n`
- `%s:IOAccessoryConfigStreamInterface::%s _numCategories %d, ret %x \n`
- `%s:IOAccessoryConfigStreamInterface::%s \n`
- `%s:IOAccessoryConfigStreamInterface::%s Enter \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID/Index %x/%d, propertyID/Index %x/%d, forceSendRequest %d, ret %x\n`
- `%s:IOAccessoryConfigStreamInterface::%s \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID %x, categoryIndex %d\n`
- `[ERROR] %s:IOAccessoryConfigStreamInterface::%s RetCategoryInfo: Failed to allocate buffer for category(%x) property data !!! \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, propertyIndex %d, numProperties %llu\n`
- `%s:IOAccessoryConfigStreamInterface::%s type %x\n`
- `%s:IOAccessoryConfigStreamInterface::%s catIndex %d, Failed to publish all DevInfo \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, _numCategories %d, numProperties %llu, propertyID %x\n`
- `[ERROR] %s:IOAccessoryConfigStreamInterface::%s %llu bytes > UINT32_MAX! \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, propertyID %x, propertyIndex %d\n`
- `%s:IOAccessoryConfigStreamInterface::%s _initialRetrievalFinished %d, _numCategories %d, categoryID/Index %x/%d, propertyID/Index %x/%d\n`
- `[ERROR] %s:IOAccessoryConfigStreamInterface::%s RetCategoryInfo: index %d, categoryID %x, numProperties %llu, CatgoryIndex too large (max %d) \n`
- `%s:IOAccessoryConfigStreamInterface::%s propertyChange: auth passed %d, failed %d\n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d / %d, categoryID %x, numProperties %u \n`
- `%s:IOAccessoryConfigStreamInterface::%s RetPropertyData: Finished retrieving all property data for categoryID %x \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, propertyIndex %d\n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID %x, catIndex %d / %d, numProp %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, propertyIndex %d / %llu, propertyID %x (%llu bytes) \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID/Index %x/%d, propertyID/Index %x/%d\n`
- `%s:IOAccessoryConfigStreamInterface::%s catIndex %d, Failed to publish all MFiDevInfo \n`
- `%s:IOAccessoryConfigStreamInterface::%s [%d/%d] categoryID %x ?= %x\n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, propertyIndex %d, propertyID %x\n`
- `[ERROR] %s:IOAccessoryConfigStreamInterface::%s RetCategoryInfo: index %d, categoryID %x, numProperties %llu, Invalid # of properties !!! (max %d) \n`
- `%s:IOAccessoryConfigStreamInterface::%s [%d/%llu] propertyID %x ?= %x\n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID/Index %x/%d, propertyID/Index %x/%d, forceSendRequest %d, waitForResponse %d\n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID %x \n`
- `[ERROR] %s:IOAccessoryConfigStreamInterface::%s RetPropertyData: Error getting propertyID for catIndex %d, propIndex %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryID %x, _numCategories %d\n`
- `%s:IOAccessoryConfigStreamInterface::%s catIndex %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s _initialRetrievalFinished %d, _numCategories %d, categoryID/Index %x/%d, propertyID/Index %x/%d, infoDataLen %llu\n`
- `%s:IOAccessoryConfigStreamInterface::%s Unknown propertyID(%x) \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d, _numCategories %d, propertyID %x\n`
- `[ERROR] %s:IOAccessoryConfigStreamInterface::%s RetDevInfo: numCategories(%d) too large! limit to %d \n`
- `%s:IOAccessoryConfigStreamInterface::%s categoryIndex %d / %d, categoryID %x, propertyIndex %d /%d, valid %d \n`
