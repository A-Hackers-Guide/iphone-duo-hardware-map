# `CAInterAppAudioSwitcherView`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIScrollViewDelegate`
- 7 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
^{OpaqueAudioComponentInstance=} outputUnit;
@"CAIAANodeContainer" nodeView;
@"UIPageControl" pageControl;
@"CAIAANodeInfo" info;
@"NSTimer" refreshTimer;
B showingAppNames;
B isHostConnected;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,GisShowingAppNames) showingAppNames;
```

## Instance methods

```
-[CAInterAppAudioSwitcherView startTimer];
-[CAInterAppAudioSwitcherView observeValueForKeyPath:ofObject:change:context:];
-[CAInterAppAudioSwitcherView initialize];
-[CAInterAppAudioSwitcherView layoutSubviews];
-[CAInterAppAudioSwitcherView removeFromSuperview];
-[CAInterAppAudioSwitcherView contentWidth];
-[CAInterAppAudioSwitcherView initWithCoder:];
-[CAInterAppAudioSwitcherView scrollViewDidEndDecelerating:];
-[CAInterAppAudioSwitcherView didMoveToSuperview];
-[CAInterAppAudioSwitcherView initWithFrame:];
-[CAInterAppAudioSwitcherView updateInfo];
-[CAInterAppAudioSwitcherView isHostConnected];
-[CAInterAppAudioSwitcherView appHasGoneForeground];
-[CAInterAppAudioSwitcherView appHasGoneInBackground];
-[CAInterAppAudioSwitcherView audioUnitPropertyChangedListener:unit:propID:scope:element:];
-[CAInterAppAudioSwitcherView changePage:];
-[CAInterAppAudioSwitcherView isShowingAppNames];
-[CAInterAppAudioSwitcherView nodePressed:];
-[CAInterAppAudioSwitcherView setOutputAudioUnit:];
-[CAInterAppAudioSwitcherView setShowingAppNames:];
-[CAInterAppAudioSwitcherView updateNodeList];
```
