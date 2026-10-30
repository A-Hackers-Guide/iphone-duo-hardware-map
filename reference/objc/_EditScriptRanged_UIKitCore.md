# `_EditScriptRanged`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_EditScript`
- 2 instance variables, 2 properties, 9 instance methods, 3 class methods

## Instance variables

```
q _options;
@"_EditScriptRangedAtom" _currentScriptAtom;
```

## Properties

```
@property (T@"NSString",R,N) stringA;
@property (T@"NSString",R,N) stringB;
```

## Class methods

```
+[_EditScriptRanged editScriptForSmallestSingleEditFromString:toString:];
+[_EditScriptRanged editScriptFromString:toString:];
+[_EditScriptRanged editScriptFromString:toString:chunkSize:orderAtomsAscending:operationPrecedence:options:];
```

## Instance methods

```
-[_EditScriptRanged stringA];
-[_EditScriptRanged stringB];
-[_EditScriptRanged addToCurrentScriptAtomEditOperation:editIndex:newText:indexInArrayB:];
-[_EditScriptRanged applyToString:];
-[_EditScriptRanged computeSmallestSingleEdit];
-[_EditScriptRanged finalizeCurrentScriptAtom];
-[_EditScriptRanged initWithOperationPrecedence:dataClass:chunkSize:stringA:stringB:orderAtomsAscending:options:];
-[_EditScriptRanged initializeCurrentScriptAtom];
-[_EditScriptRanged removeAnyOverlapBetweenIndexOfFirstDifference:andReverseIndexOfLastDifference:shouldShortenFirstDifference:];
```
