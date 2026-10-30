# `_EditScript`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _orderAtomsAscending;
@"_IntArray2D" _distanceMatrix;
q _currentOperation;
@"<_EditScriptData>" _itemAData;
@"<_EditScriptData>" _itemBData;
@"NSArray" _operationPrecedenceArray;
@"NSMutableArray" _script;
```

## Properties

```
@property (T@"NSArray",C,N,V_operationPrecedenceArray) operationPrecedenceArray;
@property (T@"NSMutableArray",&,N,V_script) script;
```

## Instance methods

```
-[_EditScript description];
-[_EditScript setScript:];
-[_EditScript script];
-[_EditScript addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:];
-[_EditScript computeDistanceMatrix];
-[_EditScript computeEditsFromMatrix];
-[_EditScript finalizeCurrentScriptAtom];
-[_EditScript initWithOperationPrecedence:orderAtomsAscending:];
-[_EditScript initializeCurrentScriptAtom];
-[_EditScript operationPrecedenceArray];
-[_EditScript operationPrecedenceArrayFromOperationPrecedence:];
-[_EditScript setOperationPrecedenceArray:];
```
