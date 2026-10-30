# `UIDropProposal`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _precise;
B _prefersFullSizePreview;
Q _operation;
q _preferredBadgeStyle;
```

## Properties

```
@property (TQ,N,V_operation) operation;
@property (Tq,N,G_preferredBadgeStyle,S_setPreferredBadgeStyle:,V_preferredBadgeStyle) preferredBadgeStyle;
@property (TB,N,GisPrecise,V_precise) precise;
@property (TB,N,V_prefersFullSizePreview) prefersFullSizePreview;
```

## Class methods

```
+[UIDropProposal new];
```

## Instance methods

```
-[UIDropProposal setOperation:];
-[UIDropProposal operation];
-[UIDropProposal init];
-[UIDropProposal description];
-[UIDropProposal copyWithZone:];
-[UIDropProposal _preferredBadgeStyle];
-[UIDropProposal _setPreferredBadgeStyle:];
-[UIDropProposal initWithDropOperation:];
-[UIDropProposal isPrecise];
-[UIDropProposal prefersFullSizePreview];
-[UIDropProposal setPrecise:];
-[UIDropProposal setPrefersFullSizePreview:];
```
