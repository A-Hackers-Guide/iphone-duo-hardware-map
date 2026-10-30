# `TCTokenInfo`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _tokenText;
q _tokenId;
{_NSRange="location"Q"length"Q} _range;
{_NSRange="location"Q"length"Q} _enclosingRange;
```

## Properties

```
@property (T{_NSRange=QQ},R,V_range) range;
@property (T{_NSRange=QQ},R) precedingRange;
@property (T{_NSRange=QQ},R) followingRange;
@property (T{_NSRange=QQ},R,V_enclosingRange) enclosingRange;
@property (T@"NSString",R,C,V_tokenText) tokenText;
@property (Tq,R,V_tokenId) tokenId;
```

## Instance methods

```
-[TCTokenInfo range];
-[TCTokenInfo hash];
-[TCTokenInfo description];
-[TCTokenInfo copyWithZone:];
-[TCTokenInfo isEqual:];
-[TCTokenInfo enclosingRange];
-[TCTokenInfo tokenText];
-[TCTokenInfo tokenId];
-[TCTokenInfo followingRange];
-[TCTokenInfo initWithRange:enclosingRange:tokenText:tokenId:];
-[TCTokenInfo precedingRange];
```
