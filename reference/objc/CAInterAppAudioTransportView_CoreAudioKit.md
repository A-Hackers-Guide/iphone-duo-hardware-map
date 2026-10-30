# `CAInterAppAudioTransportView`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 10 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"CAUITransportButton" rewindButton;
@"CAUITransportButton" playPauseButton;
@"CAUITransportButton" recordButton;
@"UILabel" currentTimeLabel;
@"UIColor" pauseButtonColor;
@"UIColor" playButtonColor;
^{OpaqueAudioComponentInstance=} outputUnit;
^{HostCallbackInfo=^v^?^?^?^?} callBackInfo;
@"NSTimer" pollingPlayerTimer;
B enabled;
B inForeground;
B _playing;
B _recording;
B _connected;
d _playTime;
@"UIFont" _currentTimeLabelFont;
```

## Properties

```
@property (TB,GisEnabled) enabled;
@property (TB,R,N,GisPlaying,V_playing) playing;
@property (TB,R,N,GisRecording,V_recording) recording;
@property (TB,R,N,GisConnected,V_connected) connected;
@property (T@"UIColor",&,N) labelColor;
@property (T@"UIFont",&,N,V_currentTimeLabelFont) currentTimeLabelFont;
@property (T@"UIColor",&,N) rewindButtonColor;
@property (T@"UIColor",&,N) playButtonColor;
@property (T@"UIColor",&,N) pauseButtonColor;
@property (T@"UIColor",&,N) recordButtonColor;
```

## Instance methods

```
-[CAInterAppAudioTransportView isConnected];
-[CAInterAppAudioTransportView isRecording];
-[CAInterAppAudioTransportView updateTransportControls];
-[CAInterAppAudioTransportView initialize];
-[CAInterAppAudioTransportView canPlay];
-[CAInterAppAudioTransportView dealloc];
-[CAInterAppAudioTransportView isPlaying];
-[CAInterAppAudioTransportView layoutSubviews];
-[CAInterAppAudioTransportView labelColor];
-[CAInterAppAudioTransportView togglePlayback:];
-[CAInterAppAudioTransportView isEnabled];
-[CAInterAppAudioTransportView setLabelColor:];
-[CAInterAppAudioTransportView setEnabled:];
-[CAInterAppAudioTransportView initWithCoder:];
-[CAInterAppAudioTransportView initWithFrame:];
-[CAInterAppAudioTransportView canRecord];
-[CAInterAppAudioTransportView isHostConnected];
-[CAInterAppAudioTransportView playButtonColor];
-[CAInterAppAudioTransportView appHasGoneForeground];
-[CAInterAppAudioTransportView appHasGoneInBackground];
-[CAInterAppAudioTransportView audioUnitPropertyChangedListener:unit:propID:scope:element:];
-[CAInterAppAudioTransportView canRewind];
-[CAInterAppAudioTransportView currentTimeLabelFont];
-[CAInterAppAudioTransportView getHostCallbackInfo];
-[CAInterAppAudioTransportView getPlayTimeString];
-[CAInterAppAudioTransportView pauseButtonColor];
-[CAInterAppAudioTransportView pollHost];
-[CAInterAppAudioTransportView recordButtonColor];
-[CAInterAppAudioTransportView rewindAction:];
-[CAInterAppAudioTransportView rewindButtonColor];
-[CAInterAppAudioTransportView sendStateToRemoteHost:];
-[CAInterAppAudioTransportView setCurrentTimeLabelFont:];
-[CAInterAppAudioTransportView setOutputAudioUnit:];
-[CAInterAppAudioTransportView setPauseButtonColor:];
-[CAInterAppAudioTransportView setPlayButtonColor:];
-[CAInterAppAudioTransportView setRecordButtonColor:];
-[CAInterAppAudioTransportView setRewindButtonColor:];
-[CAInterAppAudioTransportView startPollingPlayer];
-[CAInterAppAudioTransportView stopPollingPlayer];
-[CAInterAppAudioTransportView toggleRecording:];
-[CAInterAppAudioTransportView updateStatefromTransportCallBack];
```
