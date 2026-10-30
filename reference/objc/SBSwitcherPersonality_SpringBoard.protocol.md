# `SBSwitcherPersonality` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBSwitcherContextProviding`, `SBSwitcherMultitaskingQueryProviding`, `BSDescriptionProviding`, `NSObject`
- 0 instance variables, 2 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"<SBSwitcherPersonalityView>",W,N) view;
@property (T@"<SBChainableModifierDelegate>",W,N) switcherContextDelegate;
```

## Instance methods

```
-[SBSwitcherPersonality preferredSceneSizeThatFits:displayItem:];
-[SBSwitcherPersonality setSwitcherContextDelegate:];
-[SBSwitcherPersonality performWithFinalPresentationValue:];
-[SBSwitcherPersonality setView:];
-[SBSwitcherPersonality identifiersInStrip];
-[SBSwitcherPersonality viewWillLayout];
-[SBSwitcherPersonality handleEvent:responseHandler:];
-[SBSwitcherPersonality view];
-[SBSwitcherPersonality switcherContextDelegate];
-[SBSwitcherPersonality windowingStrip];
-[SBSwitcherPersonality windowingViewModelForAppLayout:];
-[SBSwitcherPersonality performWithInterfaceOrientation:block:];
-[SBSwitcherPersonality setTimelineAuditor:];
-[SBSwitcherPersonality performWithUpdateMode:block:];
-[SBSwitcherPersonality defaultFrameForLeafAppLayout:inSwitcherScreenRegion:];
```
