# `TAAudioStreamDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance methods

```
-[TAAudioStreamDelegate audioStream:didStart:error:];
-[TAAudioStreamDelegate audioStream:didPause:error:];
-[TAAudioStreamDelegate audioStream:didReceiveDTMFEventWithDigit:];
-[TAAudioStreamDelegate audioStream:didReceiveRTCPPackets:];
-[TAAudioStreamDelegate audioStream:didResume:error:];
-[TAAudioStreamDelegate audioStream:updateInputFrequencyLevel:];
-[TAAudioStreamDelegate audioStream:updateOutputFrequencyLevel:];
-[TAAudioStreamDelegate audioStreamDidRTCPTimeOut:];
-[TAAudioStreamDelegate audioStreamDidRTPTimeOut:];
-[TAAudioStreamDelegate audioStreamDidRecoverFromRTCPTimeOut:];
-[TAAudioStreamDelegate audioStreamDidServerDie:];
-[TAAudioStreamDelegate audioStreamDidStop:];
-[TAAudioStreamDelegate callAudioServiceDidCrash:];
```
