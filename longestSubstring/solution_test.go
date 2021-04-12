package longestSubstring

import "testing"

func Test_lengthOfLongestSubstring(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		args args
		want int
	}{
		{
			args: args{
				s: "abcabcbb",
			},
			want: 3,
		},
		{
			args: args{
				s: "bbbbb",
			},
			want: 1,
		},
		{
			args: args{
				s: "pwwkew",
			},
			want: 3,
		},
		{
			args: args{
				s: "",
			},
			want: 0,
		},
		{
			args: args{
				s: "au",
			},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.args.s, func(t *testing.T) {
			if got := lengthOfLongestSubstring(tt.args.s); got != tt.want {
				t.Errorf("lengthOfLongestSubstring() = %v, want %v", got, tt.want)
			}
		})
	}
}
