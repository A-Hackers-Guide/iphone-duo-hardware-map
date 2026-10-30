# `TUAudioFrequencyController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCAudioPowerSpectrumMeterDelegate`
- 3 instance variables, 7 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"<TUAudioFrequencyControllerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"AVCAudioPowerSpectrumMeter" _powerSpectrumMeter;
```

## Properties

```
@property (T@"<TUAudioFrequencyControllerDelegate>",R,W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"AVCAudioPowerSpectrumMeter",R,N,V_powerSpectrumMeter) powerSpectrumMeter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUAudioFrequencyController normalizedPowerLevelForPowerSpectrum:];
+[TUAudioFrequencyController normalizedSpectrumForPowerSpectrum:];
+[TUAudioFrequencyController rawPowerLevelForPowerSpectrum:];
```

## Instance methods

```
-[TUAudioFrequencyController initWithDelegate:queue:];
-[TUAudioFrequencyController queue];
-[TUAudioFrequencyController delegate];
-[TUAudioFrequencyController _avcTapTypeForTUTapType:];
-[TUAudioFrequencyController audioPowerSpectrumMeter:didUpdateAudioPowerSpectrums:];
-[TUAudioFrequencyController initWithDelegate:queue:binCount:];
-[TUAudioFrequencyController meterServerDidDisconnect:];
-[TUAudioFrequencyController powerSpectrumMeter];
-[TUAudioFrequencyController registerCellularPowerSpectrum:];
-[TUAudioFrequencyController registerParticipantPowerSpectrum:];
-[TUAudioFrequencyController unregisterCellularPowerSpectrum:];
-[TUAudioFrequencyController unregisterParticipantPowerSpectrum:];
```
