# `_SBSystemStatusStatusBarOverridesArchiveRecord`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 3 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"STStatusBarData" _statusBarData;
@"NSSet" _suppressedBackgroundActivityIdentifiers;
```

## Properties

```
@property (T@"STStatusBarData",C,N,V_statusBarData) statusBarData;
@property (T@"NSSet",C,N,V_suppressedBackgroundActivityIdentifiers) suppressedBackgroundActivityIdentifiers;
@property (TB,R,N,GisEmpty) empty;
```

## Class methods

```
+[_SBSystemStatusStatusBarOverridesArchiveRecord supportsSecureCoding];
```

## Instance methods

```
-[_SBSystemStatusStatusBarOverridesArchiveRecord succinctDescriptionBuilder];
-[_SBSystemStatusStatusBarOverridesArchiveRecord descriptionWithMultilinePrefix:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord succinctDescription];
-[_SBSystemStatusStatusBarOverridesArchiveRecord debugDescriptionWithMultilinePrefix:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord isEmpty];
-[_SBSystemStatusStatusBarOverridesArchiveRecord encodeWithCoder:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord hash];
-[_SBSystemStatusStatusBarOverridesArchiveRecord description];
-[_SBSystemStatusStatusBarOverridesArchiveRecord initWithCoder:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord isEqual:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord _descriptionBuilderWithMultilinePrefix:forDebug:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord descriptionBuilderWithMultilinePrefix:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord suppressedBackgroundActivityIdentifiers];
-[_SBSystemStatusStatusBarOverridesArchiveRecord initWithStatusBarData:andSuppressedBackgroundActivityIdentifiers:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord recordByApplyingRecord:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord setStatusBarData:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord setSuppressedBackgroundActivityIdentifiers:];
-[_SBSystemStatusStatusBarOverridesArchiveRecord statusBarData];
```
