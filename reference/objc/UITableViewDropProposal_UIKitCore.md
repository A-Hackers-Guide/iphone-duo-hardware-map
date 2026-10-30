# `UITableViewDropProposal`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDropProposal`
- 2 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _intent;
@"NSIndexPath" _adjustedTargetIndexPath;
```

## Properties

```
@property (Tq,N,V_intent) intent;
@property (T@"NSIndexPath",&,N,G_adjustedTargetIndexPath,S_setAdjustedTargetIndexPath:,V_adjustedTargetIndexPath) adjustedTargetIndexPath;
@property (Tq,R,N) _dropLocation;
```

## Instance methods

```
-[UITableViewDropProposal setIntent:];
-[UITableViewDropProposal intent];
-[UITableViewDropProposal _adjustedTargetIndexPath];
-[UITableViewDropProposal _dropAction];
-[UITableViewDropProposal _dropLocation];
-[UITableViewDropProposal _setAdjustedTargetIndexPath:];
-[UITableViewDropProposal _updatedDropProposalWithDropOperation:dropIntent:adjustedTargetIndexPath:];
-[UITableViewDropProposal initWithDropOperation:];
-[UITableViewDropProposal initWithDropOperation:dropLocation:];
-[UITableViewDropProposal initWithDropOperation:intent:];
```
