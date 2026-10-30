# `PKAutoRefineQueryItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 1 instance methods, 0 class methods

## Instance variables

```
{vector<CGRect, std::allocator<CGRect>>="__begin_"^{CGRect}"__end_"^{CGRect}""{?="__cap_"^{CGRect}}} _boundingBoxForTokenColumn;
{vector<CGRect, std::allocator<CGRect>>="__begin_"^{CGRect}"__end_"^{CGRect}""{?="__cap_"^{CGRect}}} _rotatedBoundingBoxForTokenColumn;
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} _writingOrientationAngleForTokenColumn;
@"CHTokenizedTextResult" _textResult;
@"NSIndexSet" _refinedTokenColumns;
@"NSArray" _strokeIdentifiers;
@"NSArray" _strokesUUIDs;
@"NSIndexSet" _refinableStrokes;
@"NSLocale" _locale;
```

## Properties

```
@property (T@"NSIndexSet",C,N,V_refinedTokenColumns) refinedTokenColumns;
```

## Instance methods

```
-[PKAutoRefineQueryItem setRefinedTokenColumns:];
```
