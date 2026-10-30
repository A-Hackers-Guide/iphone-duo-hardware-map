# `_ANEWeight`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"NSString" _weightSymbol;
@"NSURL" _weightURL;
@"NSData" _SHACode;
@"NSString" _sandboxExtension;
```

## Properties

```
@property (T@"NSURL",C,N,V_weightURL) weightURL;
@property (T@"NSString",R,C,N,V_weightSymbol) weightSymbol;
@property (T@"NSData",R,C,N,V_SHACode) SHACode;
@property (T@"NSString",C,N,V_sandboxExtension) sandboxExtension;
```

## Class methods

```
+[_ANEWeight supportsSecureCoding];
+[_ANEWeight new];
+[_ANEWeight weightWithSymbolAndURL:weightURL:];
+[_ANEWeight weightWithSymbol:];
+[_ANEWeight weightWithSymbolAndURLSHA:weightURL:SHACode:];
```

## Instance methods

```
-[_ANEWeight init];
-[_ANEWeight sandboxExtension];
-[_ANEWeight initWithWeightSymbol:];
-[_ANEWeight setWeightURL:];
-[_ANEWeight weightSymbol];
-[_ANEWeight weightURL];
-[_ANEWeight setSandboxExtension:];
-[_ANEWeight encodeWithCoder:];
-[_ANEWeight updateWeightURL:];
-[_ANEWeight SHACode];
-[_ANEWeight description];
-[_ANEWeight initWithCoder:];
-[_ANEWeight copyWithZone:];
-[_ANEWeight initWithWeightSymbolAndURLSHA:weightURL:SHACode:sandboxExtension:];
-[_ANEWeight initWithWeightSymbolAndURL:weightURL:];
```
