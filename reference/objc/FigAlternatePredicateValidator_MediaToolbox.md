# `FigAlternatePredicateValidator`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSPredicateVisitor`
- 5 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSPredicate" _predicate;
^{OpaqueFigSimpleMutex=} _mutex;
B _result;
@"NSError" _error;
B _isEvaluated;
```

## Class methods

```
+[FigAlternatePredicateValidator validateKeyPathForMinMaxQualifiers:];
```

## Instance methods

```
-[FigAlternatePredicateValidator visitPredicateOperator:];
-[FigAlternatePredicateValidator visitPredicateExpression:];
-[FigAlternatePredicateValidator visitPredicate:];
-[FigAlternatePredicateValidator validateWithError:];
-[FigAlternatePredicateValidator dealloc];
-[FigAlternatePredicateValidator initWithPredicate:];
-[FigAlternatePredicateValidator _validateKeyPath:];
-[FigAlternatePredicateValidator _allowCallingFunctionWithName:];
-[FigAlternatePredicateValidator _keyPathComponentIsAllowed:];
-[FigAlternatePredicateValidator _keyPathComponents:];
-[FigAlternatePredicateValidator _unsafeEvaluateKeyPathWithDummy:];
```
