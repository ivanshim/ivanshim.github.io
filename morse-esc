# Morse-ESC

> **Morse-ESC** is a scalable binary transport over Morse timing in which values of arbitrary size are delimited solely by timing gaps, with only zero and the escape token treated specially.

*Envisioned by Ivan Shim and ChatGPT-5.2*  
*18 January 2026*

---

## 1. Purpose

Morse-ESC defines a minimal, extensible method for transmitting binary data over standard International Morse timing without redefining Morse symbols or introducing fixed-width encodings.

It enables arbitrarily large integer values to be conveyed using timing gaps as the sole framing mechanism, while preserving Morse code as a human-timed signaling layer.

---

## 2. Signaling Layer

Morse-ESC relies entirely on standard International Morse timing:

- Dot (`.`): 1 time unit  
- Dash (`-`): 3 time units  
- Intra-bit gap: 1 unit  
- Inter-value gap: 3 units  
- Inter-word gap: 7 units  

No additional symbols or timing rules are introduced.

---

## 3. Modes of Operation

Two interpretation modes exist:

- **Normal mode**: Signals are interpreted as standard International Morse Code.
- **Binary mode**: Signals are interpreted as binary values.

The system begins in normal mode.

---

## 4. Escape Token (ESC)

The sequence:


(four consecutive dashes, delimited by an inter-value gap) is reserved as the **ESC token**.

- In normal mode, `ESC` switches the decoder into binary mode.
- In binary mode, `ESC` switches the decoder back to normal mode.

The `ESC` token has no semantic meaning as a data value.

---

## 5. Binary Alphabet

In binary mode:

- Dot (`.`) represents binary **0**
- Dash (`-`) represents binary **1**

Bits are transmitted most-significant-bit first.

---

## 6. Value Delimitation and Scalability

- A **binary value** is any non-empty sequence of bits (`.` and `-`).
- A value is terminated by an **inter-value gap** (3 units).
- There is **no fixed bit width**.
- Values may contain an arbitrary number of bits.

Value boundaries are determined solely by timing gaps.

---

## 7. Canonical Encoding Rules

- Binary values are interpreted as unsigned integers.
- All non-zero values **must not contain leading zeros**.
  - The first bit of any non-zero value must therefore be `-` (binary 1).

This guarantees that each value has exactly one canonical representation.

---

## 8. Special Cases

### 8.1 Zero

- The integer value **0** is encoded as a single dot:

```.```

- No other encoding represents zero.

---

### 8.2 Escaping the Escape

- The bit pattern corresponding to `ESC` (`1111`) is reserved.
- To transmit this value as data, the escape token must be **doubled**:


- In binary mode, `ESC ESC` is interpreted as a single literal ESC data value, not as a mode switch.

This mechanism is analogous to escaping a quotation mark or backslash in programming languages.

---

## 9. Token Recognition Rule

- The `ESC` token is recognized **only at value boundaries** (i.e., immediately following an inter-value gap).
- Bit patterns occurring within a value are never interpreted as control tokens.

---

## 10. Abort / Resynchronization

To support recovery from timing errors, miscounts, or panic situations, Morse-ESC defines an explicit abort mechanism.

- A **run of three or more consecutive ESC tokens** at value boundaries SHALL be interpreted as **ABORT / RESYNC**.

Upon receiving an abort sequence, the decoder SHALL:

- Immediately discard any partially received value
- Exit binary mode if currently active
- Return to **normal Morse mode**
- Treat the next non-ESC symbol as the start of a new, clean context

The exact number of ESC tokens beyond three is irrelevant; any run of length three or greater has identical abort semantics.

---

## 11. Error Conditions

The following conditions are invalid:

- An empty value
- A non-zero value with leading zeros
- A solitary `ESC` in binary mode not followed by either data or another `ESC`

On error, a decoder may resynchronize by waiting for a valid abort sequence or a subsequent mode transition.

---

## 12. Architectural Interpretation

- Morse timing functions as the **physical and framing layer**.
- Normal Morse symbols form a **symbolic encoding layer**.
- Binary mode defines a **self-delimiting, arbitrarily scalable integer transport** over Morse timing.

Morse-ESC does not redefine International Morse Code; it overlays a reversible escape mechanism on top of it.

---

## 13. Scope and Intent

Morse-ESC is intended for experimentation, archival signaling, and machine-assisted decoding. It demonstrates that Morse timing alone is sufficient to support scalable data transport without expanding the Morse symbol table.

---

*End of document*
