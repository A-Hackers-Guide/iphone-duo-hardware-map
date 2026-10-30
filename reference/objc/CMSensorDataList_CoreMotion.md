# `CMSensorDataList`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 19 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"CMSensorRecorderInternal" fProxy;
@"NSObject<OS_xpc_object>" fDataBuffer;
@"CLSensorRecorderSensorMeta" fCurrentBlock;
Q fCurrentBlockIdentifier;
q fCurrentBlockDataIdentifier;
d fCurrentBlockStartTime;
Q fCurrentBlockTimestamp;
* fDataBufferPtr;
Q fDataBufferLength;
Q fCurrentIdentifier;
Q fStartingIdentifier;
q fRetrievedDataBufferIdentifier;
Q fBlockOffset;
{AccelUnpacker="fData"*"fDataEnd"*"fBitsLeft"I"fPartial"C"fOverrun"B"fTimestampLast"Q"fTimestampLastDelta"q"fSampleLast"[3i]} fAccelUnpacker;
{GyroUnpacker="fData"*"fDataEnd"*"fBitsLeft"I"fPartial"C"fOverrun"B"fTimestampLast"Q"fTimestampLastDelta"q"fSampleLast"[4i]} fGyroUnpacker;
{PressureUnpacker="fData"*"fDataEnd"*"fBitsLeft"I"fPartial"C"fOverrun"B"fTimestampLast"Q"fTimestampLastDelta"q"fSampleLast"[2i]} fPressureUnpacker;
@"NSMutableArray" fCachedData;
@"NSArray" fMetaArray;
i fDataType;
```

## Instance methods

```
-[CMSensorDataList dealloc];
-[CMSensorDataList countByEnumeratingWithState:objects:count:];
-[CMSensorDataList _updatePointers];
-[CMSensorDataList _updateCurrentBlockProperties];
-[CMSensorDataList initFrom:to:withType:];
-[CMSensorDataList initWithIdentifier:andType:];
```
