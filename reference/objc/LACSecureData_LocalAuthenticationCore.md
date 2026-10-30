# `LACSecureData`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 17 instance methods, 4 class methods

## Instance variables

```
Q _allocatedLength;
^v _bytes;
Q _bytesLength;
```

## Class methods

```
+[LACSecureData resetBytes:length:];
+[LACSecureData secureDataWithBytes:length:];
+[LACSecureData secureDataWithData:];
+[LACSecureData secureDataWithString:];
```

## Instance methods

```
-[LACSecureData initWithString:];
-[LACSecureData initWithBytes:length:];
-[LACSecureData appendBytes:length:];
-[LACSecureData appendData:];
-[LACSecureData init];
-[LACSecureData data];
-[LACSecureData dealloc];
-[LACSecureData reset];
-[LACSecureData length];
-[LACSecureData appendString:];
-[LACSecureData initWithData:];
-[LACSecureData isEqual:];
-[LACSecureData bytes];
-[LACSecureData resize:];
-[LACSecureData nullTerminatedCopy];
-[LACSecureData prepareBuffer:];
-[LACSecureData removeLastCharacter];
```
