# `_UICommandMenuInsertion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UICommandChange`
- 5 instance variables, 6 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _fallbacks;
@"NSArray" _insertsAtStart;
@"NSArray" _insertsAtEnd;
@"NSArray" _insertsBefore;
@"NSArray" _insertsAfter;
```

## Properties

```
@property (T@"NSString",R,D,N) anchor;
@property (T@"NSArray",R,N,V_fallbacks) fallbacks;
@property (T@"NSArray",R,N,V_insertsAtStart) insertsAtStart;
@property (T@"NSArray",R,N,V_insertsAtEnd) insertsAtEnd;
@property (T@"NSArray",R,N,V_insertsBefore) insertsBefore;
@property (T@"NSArray",R,N,V_insertsAfter) insertsAfter;
```

## Class methods

```
+[_UICommandMenuInsertion supportsSecureCoding];
+[_UICommandMenuInsertion insertionWithAnchor:fallbacks:insertsAtStart:insertsAtEnd:insertsBefore:insertsAfter:];
```

## Instance methods

```
-[_UICommandMenuInsertion encodeWithCoder:];
-[_UICommandMenuInsertion initWithCoder:];
-[_UICommandMenuInsertion acceptBoolItemInsertionVisit:itemDeletionVisit:menuInsertionVisit:menuDeletionVisit:];
-[_UICommandMenuInsertion acceptItemInsertionVisit:itemDeletionVisit:menuInsertionVisit:menuDeletionVisit:];
-[_UICommandMenuInsertion fallbacks];
-[_UICommandMenuInsertion initWithAnchor:fallbacks:insertsAtStart:insertsAtEnd:insertsBefore:insertsAfter:];
-[_UICommandMenuInsertion insertsAfter];
-[_UICommandMenuInsertion insertsAtEnd];
-[_UICommandMenuInsertion insertsAtStart];
-[_UICommandMenuInsertion insertsBefore];
```
