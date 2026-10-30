# `SBFluidSwitcherModifierTimelineViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBFluidSwitcherModifierTimelineEntryViewDelegate`
- 9 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _entryViews;
B _isPaused;
@"SBFTouchPassThroughScrollView" _scrollView;
@"UIButton" _clearButton;
@"UIButton" _noiseLevelButton;
@"UIButton" _pauseButton;
@"UINavigationController" _navigationController;
@"SBModifierTimelineDetailViewController" _detailViewController;
B _ignoreNoisyEvents;
```

## Properties

```
@property (TB,R,N,V_ignoreNoisyEvents) ignoreNoisyEvents;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherModifierTimelineViewController addEntry:];
-[SBFluidSwitcherModifierTimelineViewController viewDidAppear:];
-[SBFluidSwitcherModifierTimelineViewController loadView];
-[SBFluidSwitcherModifierTimelineViewController viewWillLayoutSubviews];
-[SBFluidSwitcherModifierTimelineViewController _reset:];
-[SBFluidSwitcherModifierTimelineViewController _toggleNoiseLevel:];
-[SBFluidSwitcherModifierTimelineViewController _togglePause:];
-[SBFluidSwitcherModifierTimelineViewController didSelectEntryView:];
-[SBFluidSwitcherModifierTimelineViewController ignoreNoisyEvents];
```
