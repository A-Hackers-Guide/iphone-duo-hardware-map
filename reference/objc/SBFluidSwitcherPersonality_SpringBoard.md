# `SBFluidSwitcherPersonality`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- Protocols: `SBSwitcherPersonality`
- 2 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<SBSwitcherPersonalityView>" _view;
@"SBSwitcherModifier" _rootModifier;
```

## Properties

```
@property (T@"SBSwitcherModifier",R,N,V_rootModifier) rootModifier;
@property (T@"<SBSwitcherPersonalityView>",W,N,V_view) view;
@property (T@"<SBChainableModifierDelegate>",W,N) switcherContextDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherPersonality preferredSceneSizeThatFits:displayItem:];
-[SBFluidSwitcherPersonality initWithRootModifier:];
-[SBFluidSwitcherPersonality succinctDescriptionBuilder];
-[SBFluidSwitcherPersonality setSwitcherContextDelegate:];
-[SBFluidSwitcherPersonality performWithFinalPresentationValue:];
-[SBFluidSwitcherPersonality setView:];
-[SBFluidSwitcherPersonality identifiersInStrip];
-[SBFluidSwitcherPersonality descriptionWithMultilinePrefix:];
-[SBFluidSwitcherPersonality viewWillLayout];
-[SBFluidSwitcherPersonality succinctDescription];
-[SBFluidSwitcherPersonality rootModifier];
-[SBFluidSwitcherPersonality handleEvent:responseHandler:];
-[SBFluidSwitcherPersonality view];
-[SBFluidSwitcherPersonality switcherContextDelegate];
-[SBFluidSwitcherPersonality windowingStrip];
-[SBFluidSwitcherPersonality windowingViewModelForAppLayout:];
-[SBFluidSwitcherPersonality performWithInterfaceOrientation:block:];
-[SBFluidSwitcherPersonality description];
-[SBFluidSwitcherPersonality setTimelineAuditor:];
-[SBFluidSwitcherPersonality performWithUpdateMode:block:];
-[SBFluidSwitcherPersonality descriptionBuilderWithMultilinePrefix:];
```
