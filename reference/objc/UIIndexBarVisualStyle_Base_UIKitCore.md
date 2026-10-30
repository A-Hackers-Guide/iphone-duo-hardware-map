# `UIIndexBarVisualStyle_Base`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIIndexBarVisualStyle`
- 1 instance variables, 12 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"UIIndexBarView" _indexBarView;
```

## Properties

```
@property (T@"UIIndexBarView",W,N,V_indexBarView) indexBarView;
@property (TB,R,N) canBecomeFocused;
@property (TB,R,N) overlay;
@property (Td,R,N) minLineHeight;
@property (Td,R,N) indexWidth;
@property (Td,R,N) lineSpacing;
@property (TB,?,N) expanded;
@property (Td,?,R,N) trackingChangeHysteresis;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIIndexBarVisualStyle_Base containerViewForIndexBar:];
```

## Instance methods

```
-[UIIndexBarVisualStyle_Base initWithView:];
-[UIIndexBarVisualStyle_Base canBecomeFocused];
-[UIIndexBarVisualStyle_Base sizeThatFits:];
-[UIIndexBarVisualStyle_Base overlay];
-[UIIndexBarVisualStyle_Base lineSpacing];
-[UIIndexBarVisualStyle_Base renderingHeightForDisplayEntry:];
-[UIIndexBarVisualStyle_Base _indexForEntryAtPoint:];
-[UIIndexBarVisualStyle_Base _visibleBoundsForRect:stride:];
-[UIIndexBarVisualStyle_Base displayEntryFromEntry:];
-[UIIndexBarVisualStyle_Base handleTouch:withEvent:touchedEntryIndex:];
-[UIIndexBarVisualStyle_Base indexBarView];
-[UIIndexBarVisualStyle_Base indexWidth];
-[UIIndexBarVisualStyle_Base minLineHeight];
-[UIIndexBarVisualStyle_Base setIndexBarView:];
```
