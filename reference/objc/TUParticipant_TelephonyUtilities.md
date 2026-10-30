# `TUParticipant`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 3 properties, 17 instance methods, 3 class methods

## Instance variables

```
@"NSString" _name;
@"TUSandboxExtendedURL" _sandboxExtendedImageURL;
```

## Properties

```
@property (T@"NSURL",&,N) imageURL;
@property (T@"NSString",C,N,V_name) name;
@property (T@"TUSandboxExtendedURL",&,N,V_sandboxExtendedImageURL) sandboxExtendedImageURL;
```

## Class methods

```
+[TUParticipant supportsSecureCoding];
+[TUParticipant unarchivedObjectClasses];
+[TUParticipant unarchivedObjectFromData:error:];
```

## Instance methods

```
-[TUParticipant imageURL];
-[TUParticipant mutableCopyWithZone:];
-[TUParticipant initWithParticipant:];
-[TUParticipant archivedDataWithError:];
-[TUParticipant isEqualToParticipant:];
-[TUParticipant encodeWithCoder:];
-[TUParticipant hash];
-[TUParticipant description];
-[TUParticipant setName:];
-[TUParticipant initWithCoder:];
-[TUParticipant copyWithZone:];
-[TUParticipant isEqual:];
-[TUParticipant setImageURL:];
-[TUParticipant name];
-[TUParticipant initWithName:];
-[TUParticipant sandboxExtendedImageURL];
-[TUParticipant setSandboxExtendedImageURL:];
```
