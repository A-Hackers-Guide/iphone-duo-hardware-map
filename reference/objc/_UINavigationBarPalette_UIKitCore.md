# `_UINavigationBarPalette`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`, `_UINavigationBarLayoutParticipating`
- 11 instance variables, 15 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _transitioning;
B _pinned;
B __displaysWhenSearchActive;
@"UIView" _contentView;
d _preferredHeight;
d _minimumHeight;
@"NSString" _assistantIdentifier;
@"_UIPointerInteractionAssistant" _assistant;
@"UINavigationItem" _owningNavigationItem;
Q __contentViewMarginType;
q __layoutPriority;
```

## Properties

```
@property (T@"NSString",C,N,V_assistantIdentifier) assistantIdentifier;
@property (T@"_UIPointerInteractionAssistant",W,N,V_assistant) assistant;
@property (TB,N,V_transitioning) transitioning;
@property (TB,N,GisPinned,V_pinned) pinned;
@property (T@"UINavigationItem",W,N,V_owningNavigationItem) owningNavigationItem;
@property (TQ,N,S_setContentViewMarginType:,V__contentViewMarginType) _contentViewMarginType;
@property (TB,N,S_setDisplaysWhenSearchActive:,V__displaysWhenSearchActive) _displaysWhenSearchActive;
@property (Tq,N,S_setLayoutPriority:,V__layoutPriority) _layoutPriority;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (Td,N,V_preferredHeight) preferredHeight;
@property (Td,N,V_minimumHeight) minimumHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarPalette assistant];
-[_UINavigationBarPalette _setAssistants];
-[_UINavigationBarPalette _clearAssistants];
-[_UINavigationBarPalette setAssistant:];
-[_UINavigationBarPalette initWithContentView:];
-[_UINavigationBarPalette setMinimumHeight:];
-[_UINavigationBarPalette setPinned:];
-[_UINavigationBarPalette isPinned];
-[_UINavigationBarPalette addSubview:];
-[_UINavigationBarPalette pointerInteraction:styleForRegion:];
-[_UINavigationBarPalette setHidden:];
-[_UINavigationBarPalette preferredHeight];
-[_UINavigationBarPalette assistantIdentifier];
-[_UINavigationBarPalette init];
-[_UINavigationBarPalette updateLayoutData:layoutWidth:];
-[_UINavigationBarPalette pointerInteraction:willEnterRegion:animator:];
-[_UINavigationBarPalette pointerInteraction:willExitRegion:animator:];
-[_UINavigationBarPalette minimumHeight];
-[_UINavigationBarPalette layoutSubviews];
-[_UINavigationBarPalette pointerInteraction:regionForRequest:defaultRegion:];
-[_UINavigationBarPalette contentView];
-[_UINavigationBarPalette description];
-[_UINavigationBarPalette setTransitioning:];
-[_UINavigationBarPalette setAssistantIdentifier:];
-[_UINavigationBarPalette transitioning];
-[_UINavigationBarPalette setPreferredHeight:];
-[_UINavigationBarPalette _layoutPriority];
-[_UINavigationBarPalette _contentViewMarginType];
-[_UINavigationBarPalette _displaysWhenSearchActive];
-[_UINavigationBarPalette _setContentViewMarginType:];
-[_UINavigationBarPalette _setDisplaysWhenSearchActive:];
-[_UINavigationBarPalette _setLayoutPriority:];
-[_UINavigationBarPalette owningNavigationItem];
-[_UINavigationBarPalette setOwningNavigationItem:];
```
