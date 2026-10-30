# `CoreTelephonyClientSMSDelegateInternal` (protocol)

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance methods

```
-[CoreTelephonyClientSMSDelegateInternal smsMessageClass0Received:body:address:];
-[CoreTelephonyClientSMSDelegateInternal mmsConfigurationChangedNotification:changed:];
-[CoreTelephonyClientSMSDelegateInternal mmsMessageReceived:msgID:];
-[CoreTelephonyClientSMSDelegateInternal mmsMessageReceivedDeferred:msgID:];
-[CoreTelephonyClientSMSDelegateInternal postMMSMessageSent:success:messageID:err1:err2:];
-[CoreTelephonyClientSMSDelegateInternal postMessageProgressNotification:messageID:totalBytesSent:dataLength:];
-[CoreTelephonyClientSMSDelegateInternal postMmsDataActivationFailed:failureNotification:];
-[CoreTelephonyClientSMSDelegateInternal postSMSMessageSent:success:messageID:err1:err2:];
-[CoreTelephonyClientSMSDelegateInternal postSUPLInitNotification:body:];
-[CoreTelephonyClientSMSDelegateInternal postSUPLInitNotification:data:];
-[CoreTelephonyClientSMSDelegateInternal postSmscAddressAvailable:smsc:];
-[CoreTelephonyClientSMSDelegateInternal smsConditionsChanged:changeMask:];
-[CoreTelephonyClientSMSDelegateInternal smsMessageCellBroadcastReceived:notificationDict:additionalDict:];
-[CoreTelephonyClientSMSDelegateInternal smsMessageReceived:msgID:];
-[CoreTelephonyClientSMSDelegateInternal smsMessageReceivedDeferred:msgID:];
-[CoreTelephonyClientSMSDelegateInternal smsReadyStateChanged:info:];
-[CoreTelephonyClientSMSDelegateInternal smsSent:messageID:info:];
```
