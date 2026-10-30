# `CTLazuliChatBotCardLayout`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _cardOrientation;
q _imageAlignment;
@"CTLazuliMessageChatBotTitleStyle" _titleStyle;
@"CTLazuliMessageChatBotDescriptionStyle" _descriptionStyle;
@"CTLazuliMessageChatBotCardStyle" _cardStyle;
```

## Properties

```
@property (Tq,N,V_cardOrientation) cardOrientation;
@property (Tq,N,V_imageAlignment) imageAlignment;
@property (T@"CTLazuliMessageChatBotTitleStyle",&,N,V_titleStyle) titleStyle;
@property (T@"CTLazuliMessageChatBotDescriptionStyle",&,N,V_descriptionStyle) descriptionStyle;
@property (T@"CTLazuliMessageChatBotCardStyle",&,N,V_cardStyle) cardStyle;
```

## Class methods

```
+[CTLazuliChatBotCardLayout supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliChatBotCardLayout setTitleStyle:];
-[CTLazuliChatBotCardLayout encodeWithCoder:];
-[CTLazuliChatBotCardLayout description];
-[CTLazuliChatBotCardLayout initWithCoder:];
-[CTLazuliChatBotCardLayout copyWithZone:];
-[CTLazuliChatBotCardLayout isEqual:];
-[CTLazuliChatBotCardLayout imageAlignment];
-[CTLazuliChatBotCardLayout cardOrientation];
-[CTLazuliChatBotCardLayout cardStyle];
-[CTLazuliChatBotCardLayout descriptionStyle];
-[CTLazuliChatBotCardLayout initWithReflection:];
-[CTLazuliChatBotCardLayout isEqualToCTLazuliChatBotCardLayout:];
-[CTLazuliChatBotCardLayout setCardOrientation:];
-[CTLazuliChatBotCardLayout setCardStyle:];
-[CTLazuliChatBotCardLayout setDescriptionStyle:];
-[CTLazuliChatBotCardLayout setImageAlignment:];
-[CTLazuliChatBotCardLayout titleStyle];
```
