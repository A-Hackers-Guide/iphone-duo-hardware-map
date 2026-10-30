# `UITableCellAccessoryLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UICellAccessoryLayout`
- 11 instance variables, 17 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"UICellAccessoryManager" _manager;
Q _edge;
d _safeAreaInset;
@? _standardLayoutWidthProvider;
@? _disclosureLayoutWidthProvider;
@? _spacingBlock;
@"NSDictionary" _initialFrames;
@"NSDictionary" _finalFrames;
@"NSMutableDictionary" _initialAlphas;
@"NSMutableDictionary" _finalAlphas;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _totalFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_totalFrame) totalFrame;
@property (T@"NSDictionary",&,N,V_initialFrames) initialFrames;
@property (T@"NSDictionary",&,N,V_finalFrames) finalFrames;
@property (T@"NSMutableDictionary",&,N,V_initialAlphas) initialAlphas;
@property (T@"NSMutableDictionary",&,N,V_finalAlphas) finalAlphas;
@property (Td,R,N) _standardLayoutWidth;
@property (Td,R,N) _disclosureLayoutWidth;
@property (T@?,C,N,V_spacingBlock) spacingBlock;
@property (T@"UICellAccessoryManager",W,N,V_manager) manager;
@property (Td,N,V_safeAreaInset) safeAreaInset;
@property (TQ,N,V_edge) edge;
@property (T@?,C,N,V_standardLayoutWidthProvider) standardLayoutWidthProvider;
@property (T@?,C,N,V_disclosureLayoutWidthProvider) disclosureLayoutWidthProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITableCellAccessoryLayout setEdge:];
-[UITableCellAccessoryLayout totalFrame];
-[UITableCellAccessoryLayout edge];
-[UITableCellAccessoryLayout initialFrames];
-[UITableCellAccessoryLayout init];
-[UITableCellAccessoryLayout setManager:];
-[UITableCellAccessoryLayout finalAlphas];
-[UITableCellAccessoryLayout setDisclosureLayoutWidthProvider:];
-[UITableCellAccessoryLayout prepareLayoutForAccessories:previousAccessories:configurationIdentifier:animated:];
-[UITableCellAccessoryLayout setInitialAlphas:];
-[UITableCellAccessoryLayout endLayout];
-[UITableCellAccessoryLayout setInitialFrames:];
-[UITableCellAccessoryLayout initialFrameForAccessory:];
-[UITableCellAccessoryLayout manager];
-[UITableCellAccessoryLayout finalFrameForAccessory:];
-[UITableCellAccessoryLayout initialAlphaForAccessory:];
-[UITableCellAccessoryLayout _layoutWidthForAccessory:withItemWidth:];
-[UITableCellAccessoryLayout _disclosureLayoutWidth];
-[UITableCellAccessoryLayout _framesForAccessories:withContainerSize:outTotalFrame:];
-[UITableCellAccessoryLayout setFinalAlphas:];
-[UITableCellAccessoryLayout setStandardLayoutWidthProvider:];
-[UITableCellAccessoryLayout setFinalFrames:];
-[UITableCellAccessoryLayout finalAlphaForAccessory:];
-[UITableCellAccessoryLayout _standardLayoutWidth];
-[UITableCellAccessoryLayout _frameForAccessoryAtIndex:inAccessories:containerSize:withXOrigin:];
-[UITableCellAccessoryLayout disclosureLayoutWidthProvider];
-[UITableCellAccessoryLayout setSafeAreaInset:];
-[UITableCellAccessoryLayout _totalWidthForAccessories:withContainerSize:];
-[UITableCellAccessoryLayout standardLayoutWidthProvider];
-[UITableCellAccessoryLayout setTotalFrame:];
-[UITableCellAccessoryLayout initialAlphas];
-[UITableCellAccessoryLayout spacingBlock];
-[UITableCellAccessoryLayout setSpacingBlock:];
-[UITableCellAccessoryLayout safeAreaInset];
-[UITableCellAccessoryLayout finalFrames];
```
