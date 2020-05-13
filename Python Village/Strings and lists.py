'''
Problem
  Given: A string s of length at most 200 letters and four integers a, b, c and d.
  Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.  In other words, we should include elements s[b] and s[d] in our slice.
'''

'''
6i0kGfX8RSwYasDgPXPpP6zwZBqkFgyKrQvEZUWxYaKkdZvkpdiHydrosaurusbcahrJYUddu9fIHYmZofakFmvJPMEVRSD6lAykMPYJcWMnYaqcgNpAaizUozMYyVUHUTfasciolatawLASnCsd7wp5a7VKKF8yz5aLYka7kU0.
51 61 130 139
'''

s = '6i0kGfX8RSwYasDgPXPpP6zwZBqkFgyKrQvEZUWxYaKkdZvkpdiHydrosaurusbcahrJYUddu9fIHYmZofakFmvJPMEVRSD6lAykMPYJcWMnYaqcgNpAaizUozMYyVUHUTfasciolatawLASnCsd7wp5a7VKKF8yz5aLYka7kU0.'
s[51:61+1] + ' ' + s[130:139+1]
# 'Hydrosaurus fasciolata'
