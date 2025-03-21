import pygame
import os

pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

bg = pygame.image.load("music_image/cas.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

pygame.font.init()
font = pygame.font.Font(None, 36)

music_folder = r"C:\Users\Iznhu\Desktop\ПП2\new_folder\labs\lab7\musics"
music_files = sorted([f for f in os.listdir(music_folder) if f.endswith(".mp3")])

if not music_files:
    print("No music files found.")
    pygame.quit()
    exit()

current_track = 0
pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
pygame.mixer.music.play()

running = True
while running:
    screen.blit(bg, (0, 0))

    song_name = music_files[current_track]
    text = font.render(f"{song_name}", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
                pygame.mixer.music.play()
pygame.quit()