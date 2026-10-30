# `SBFluidSwitcherModifierTimelineEntryView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _nameLabel;
@"UILabel" _postStackLabel;
@"UILabel" _actionsLabel;
@"UITapGestureRecognizer" _tapRecognizer;
@"SBSwitcherModifierTimelineEntry" _entry;
@"<SBFluidSwitcherModifierTimelineEntryViewDelegate>" _delegate;
```

## Properties

```
@property (T@"SBSwitcherModifierTimelineEntry",&,N,V_entry) entry;
@property (T@"<SBFluidSwitcherModifierTimelineEntryViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBFluidSwitcherModifierTimelineEntryView layoutSubviews];
-[SBFluidSwitcherModifierTimelineEntryView setDelegate:];
-[SBFluidSwitcherModifierTimelineEntryView delegate];
-[SBFluidSwitcherModifierTimelineEntryView entry];
-[SBFluidSwitcherModifierTimelineEntryView _tap:];
-[SBFluidSwitcherModifierTimelineEntryView setEntry:];
-[SBFluidSwitcherModifierTimelineEntryView _appendRecursiveDescriptionToString:level:snapshot:];
-[SBFluidSwitcherModifierTimelineEntryView _attributedStringsForStack:];
-[SBFluidSwitcherModifierTimelineEntryView _randomColorWithSeed:];
-[SBFluidSwitcherModifierTimelineEntryView _randomFloatFromSeed:min:max:];
-[SBFluidSwitcherModifierTimelineEntryView initWithFrame:entry:];
```
