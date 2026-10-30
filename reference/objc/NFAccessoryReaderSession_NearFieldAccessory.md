# `NFAccessoryReaderSession`

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFAccessorySession`
- Protocols: `NFReaderSessionAccessoryCallbacks`
- 1 instance variables, 5 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"<NFAccessoryReaderSessionDelegate>" _delegate;
```

## Properties

```
@property (T@"<NFAccessoryReaderSessionDelegate>",W) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFAccessoryReaderSession supportsSecureCoding];
```

## Instance methods

```
-[NFAccessoryReaderSession didEndUnexpectedly];
-[NFAccessoryReaderSession setDelegate:];
-[NFAccessoryReaderSession encodeWithCoder:];
-[NFAccessoryReaderSession delegate];
-[NFAccessoryReaderSession didTimeout];
-[NFAccessoryReaderSession endSessionWithCompletion:];
-[NFAccessoryReaderSession connectTag:error:];
-[NFAccessoryReaderSession stopPolling:];
-[NFAccessoryReaderSession didDetectTags:];
-[NFAccessoryReaderSession didTerminate:];
-[NFAccessoryReaderSession disconnectTag:];
-[NFAccessoryReaderSession enableContinuousWave:withFrequencySweep:];
-[NFAccessoryReaderSession sendMFGCommand:payload:error:];
-[NFAccessoryReaderSession startPollingForTechnology:error:];
-[NFAccessoryReaderSession transceive:error:];
-[NFAccessoryReaderSession readTypeIdentifier:];
-[NFAccessoryReaderSession sendAccessoryProtocolCommand:outError:];
-[NFAccessoryReaderSession setTagDataRate:];
-[NFAccessoryReaderSession checkNdefSupport:andWrite:error:];
-[NFAccessoryReaderSession checkPresence:];
-[NFAccessoryReaderSession readNDEF:];
-[NFAccessoryReaderSession sendAuthProtocolCommand:error:];
-[NFAccessoryReaderSession startLpcdPolling:];
-[NFAccessoryReaderSession startPolling:];
```
