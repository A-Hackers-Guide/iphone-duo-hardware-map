# `UIDictationWordsSeeker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _reverse;
@"NSArray" _targetStringWords;
@"NSArray" _targetSubstringWords;
@"NSString" _targetString;
@"NSString" _targetSubstring;
```

## Properties

```
@property (T@"NSArray",&,N,V_targetStringWords) targetStringWords;
@property (T@"NSArray",&,N,V_targetSubstringWords) targetSubstringWords;
@property (T@"NSString",&,N,V_targetString) targetString;
@property (T@"NSString",&,N,V_targetSubstring) targetSubstring;
@property (TB,N,V_reverse) reverse;
```

## Class methods

```
+[UIDictationWordsSeeker _isSubstringArray:equalToSubstringArray:];
+[UIDictationWordsSeeker _prepareAllWordsWithString:reverse:];
```

## Instance methods

```
-[UIDictationWordsSeeker reverse];
-[UIDictationWordsSeeker setReverse:];
-[UIDictationWordsSeeker targetSubstring];
-[UIDictationWordsSeeker _search];
-[UIDictationWordsSeeker initWithString:substring:reverse:];
-[UIDictationWordsSeeker rangeOfSubstring:fullString:reverse:];
-[UIDictationWordsSeeker setTargetString:];
-[UIDictationWordsSeeker setTargetStringWords:];
-[UIDictationWordsSeeker setTargetSubstring:];
-[UIDictationWordsSeeker setTargetSubstringWords:];
-[UIDictationWordsSeeker targetString];
-[UIDictationWordsSeeker targetStringWords];
-[UIDictationWordsSeeker targetSubstringWords];
-[UIDictationWordsSeeker validateWordBoundariesInRange:];
```
