# `_EditScriptIndexed`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_EditScript`
- 1 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"_EditScriptIndexedAtom" _currentScriptAtom;
```

## Class methods

```
+[_EditScriptIndexed editScriptFromArray:toArray:];
+[_EditScriptIndexed editScriptFromArray:toArray:orderAtomsAscending:operationPrecedence:];
```

## Instance methods

```
-[_EditScriptIndexed addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:];
-[_EditScriptIndexed applyToArray:];
-[_EditScriptIndexed finalizeCurrentScriptAtom];
-[_EditScriptIndexed initWithOperationPrecedence:dataClass:fromArray:toArray:orderAtomsAscending:];
-[_EditScriptIndexed initializeCurrentScriptAtom];
```
