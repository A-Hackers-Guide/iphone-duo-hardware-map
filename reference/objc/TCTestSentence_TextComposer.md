# `TCTestSentence`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _originalString;
@"NSArray" _grammarDetails;
```

## Properties

```
@property (T@"NSString",R,C) originalString;
@property (T@"NSString",R,C) testString;
@property (T@"NSString",R,C) finalString;
@property (T@"NSArray",R,C) grammarDetails;
```

## Class methods

```
+[TCTestSentence supportsSecureCoding];
```

## Instance methods

```
-[TCTestSentence encodeWithCoder:];
-[TCTestSentence originalString];
-[TCTestSentence hash];
-[TCTestSentence description];
-[TCTestSentence initWithCoder:];
-[TCTestSentence copyWithZone:];
-[TCTestSentence isEqual:];
-[TCTestSentence grammarDetails];
-[TCTestSentence testString];
-[TCTestSentence finalString];
-[TCTestSentence initWithOriginalString:grammarDetails:];
-[TCTestSentence initWithTestString:];
```
